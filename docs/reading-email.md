# 阅读清单不再发送邮件

每日阅读清单不再通过 Resend 发信，也没有 `resend_latest` 手动补发。
`.github/workflows/reading.yml` 仍负责抓取、生成摘要、构建网站并发布到 GitHub Pages。

已发布的中文摘要保持原来的路径和文件名：

`https://reading.fullstackjam.com/summaries/horizon-YYYY-MM-DD-zh.md`

调度、评分和本地运行见 [READING.md](../READING.md)。
