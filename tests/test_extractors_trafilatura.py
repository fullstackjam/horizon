from __future__ import annotations

import asyncio
import sys
from unittest.mock import AsyncMock, MagicMock, patch

import httpx

from src.extractors import TrafilaturaExtractor
from src.extractors.trafilatura import ARTICLE_HEADERS
from src.models import TrafilaturaExtractorConfig

URL = "https://example.com/article"


def _extractor() -> TrafilaturaExtractor:
    return TrafilaturaExtractor(TrafilaturaExtractorConfig())


def _client(text: str = "<html><body><p>Article text.</p></body></html>", status: int = 200) -> AsyncMock:
    response = MagicMock()
    response.text = text
    response.raise_for_status.return_value = None
    if status >= 400:
        response.raise_for_status.side_effect = httpx.HTTPStatusError(
            message=str(status), request=MagicMock(), response=MagicMock()
        )
    client = AsyncMock()
    client.get.return_value = response
    return client


def _trafilatura_mock(extracted: str) -> MagicMock:
    mod = MagicMock()
    mod.extract.return_value = extracted
    return mod


def test_returns_extracted_text():
    client = _client()
    with patch.dict(sys.modules, {"trafilatura": _trafilatura_mock("Extracted article text.")}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result == "Extracted article text."
    client.get.assert_awaited_once_with(
        URL,
        follow_redirects=False,
        headers=ARTICLE_HEADERS,
    )


def test_returns_none_when_trafilatura_returns_empty():
    client = _client()
    with patch.dict(sys.modules, {"trafilatura": _trafilatura_mock("")}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result is None


def test_returns_none_on_http_error():
    client = _client(status=404)
    with patch.dict(sys.modules, {"trafilatura": _trafilatura_mock("text")}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result is None


def test_returns_none_when_trafilatura_raises():
    client = _client()
    mock_traf = _trafilatura_mock("text")
    mock_traf.extract.side_effect = RuntimeError("parse error")
    with patch.dict(sys.modules, {"trafilatura": mock_traf}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result is None


def test_extract_does_not_read_metadata():
    client = _client()
    mock_traf = _trafilatura_mock("Extracted article text.")
    with patch.dict(sys.modules, {"trafilatura": mock_traf}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result == "Extracted article text."
    mock_traf.extract_metadata.assert_not_called()


def test_extract_article_returns_content_and_title():
    client = _client("<html><head><title>Ignored</title></head><body><p>Body</p></body></html>")
    mock_traf = _trafilatura_mock("Extracted article text.")
    metadata = MagicMock()
    metadata.title = "  Known Title  "
    mock_traf.extract_metadata.return_value = metadata
    with patch.dict(sys.modules, {"trafilatura": mock_traf}):
        article = asyncio.run(_extractor().extract_article(URL, client))
    assert article.content == "Extracted article text."
    assert article.title == "Known Title"
    assert article.error is None


def test_extract_article_reports_http_error():
    client = _client(status=404)
    with patch.dict(sys.modules, {"trafilatura": _trafilatura_mock("text")}):
        article = asyncio.run(_extractor().extract_article(URL, client))
    assert article.content is None
    assert article.title is None
    assert article.error
    assert "HTTPStatusError" in article.error


def test_returns_none_when_not_installed():
    client = _client()
    with patch.dict(sys.modules, {"trafilatura": None}):
        result = asyncio.run(_extractor().extract(URL, client))
    assert result is None
