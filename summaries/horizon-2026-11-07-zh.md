# Horizon 每日速递 - 2026-11-07

> 从 31 条内容中筛选出 4 条重要资讯。

---

**本期值得读**
1. [牛肉在哪里？一场并未发生的实验室培养肉革命](#item-reading-1) ⭐️ 8.8/10
2. [瑞典的工厂化住宅：美国该学什么，不该照搬什么](#item-reading-2) ⭐️ 8.5/10
3. [网络隐私的后量子未来](#item-reading-3) ⭐️ 8.2/10
4. [OpenSSH 在 musl 无 PAM 环境下的锁定账户登录漏洞](#item-reading-4) ⭐️ 8.2/10

---

## 本期值得读

<a id="item-reading-1"></a>
### [牛肉在哪里？一场并未发生的实验室培养肉革命](https://harpers.org/archive/2026/09/wheres-the-beef-lab-grown-meat-erin-somers/) ⭐️ 8.8/10

这篇《Harper’s》长篇报道从 2013 年 Mark Post 的 33 万美元培养肉汉堡写起，追踪行业融资热潮、北卡罗来纳建厂与 Believer 倒闭，并记录作者作为近二十年素食者的试吃。她不判定技术已死，而以亲历反思资本、科学与消费者欲望为何未兑现承诺。

rss · Tildes · 11月7日 00:03 · 网页正文提取

**「为什么值得读」** 最有价值的是作者把产业史与亲历并置：她到北卡罗来纳时，Believer 的工厂尚未投产便破产，随后在 Mission Barns 试吃培养肉，发现难以下咽的不只是味道，而是“知道”其来源后感官被改写。这个观察多年后仍可用于理解食品科技炒作与消费者接受度，也让她对行业前景保持保留而非定论。

**「什么时候再读」** 当培养肉再次以“气候救星”或新品身份出现，或你想判断食品科技热潮时，可重读；但文中行业状况已有后续变化，具体公司与监管进展需另查。

**标签**: `#cultivated meat`, `#food technology`, `#hype cycles`, `#venture capital`, `#personal essay`

---

<a id="item-reading-2"></a>
### [瑞典的工厂化住宅：美国该学什么，不该照搬什么](https://www.vox.com/future-perfect/509022/sweden-prefabricated-housing-affordability) ⭐️ 8.5/10

Vox 分析瑞典工厂化住宅为何能规模化：关键不只在模块化工厂，更在统一、性能导向的建筑规范与长期积累的细节规则；作者认为美国与其照搬工厂，不如先改建筑与分区法规，同时保留对可负担性效果的审慎。

rss · Tildes · 11月6日 17:12 · 网页正文提取

**「为什么值得读」** 文章最有价值之处，是把“瑞典工厂盖房”从技术奇观看成制度结果：性能导向规范、全国较统一的规则和长期细节积累，才让预制模块获得规模经济。它用木结构高层、机器人浴室模块和 Katerra 破产等例子，说明创新需要可合规路径，而非一座示范工厂；也提醒瑞典仍有住房短缺、生产率停滞和木立面防火争议。多年后仍可作为判断“该引进产品还是先改规则”的分析框架。

**「什么时候再读」** 当你讨论如何推进模块化住宅、修改建筑规范或分区规则时，可重读；但文中瑞典数据与火灾争议有时间性，且预制化未必降低瑞典成本，需结合最新政策核对。

**标签**: `#housing policy`, `#prefabricated construction`, `#building codes`, `#zoning reform`, `#manufactured housing`

---

<a id="item-reading-3"></a>
### [网络隐私的后量子未来](https://blog.cloudflare.com/vole-mole/) ⭐️ 8.2/10

文章讨论 Cloudflare 的 Privacy Pass 与 MOLE 匿名凭证如何迁移到后量子密码：用 VOLE-in-the-Head 证明配合 UOV/MAYO 多元签名构造盲签名，论证方案已接近可工程化，但仍受尺寸成本、安全证明和密码分析成熟度制约。

rss · Cloudflare Blog · 11月6日 14:00 · 网页正文提取

**「为什么值得读」** 文章的价值在于把“后量子匿名凭证可行吗”拆成可核算的工程问题：PoMFRIT 用 UOV 把盲签名展示压到 4.3KB，VOLE-IHAT/ACT 的凭证也给出 6.5KB/12KB 级估算，并说明成本主要来自 Keccak 求值。它没有回避代价：公钥达 46.6KB，one-more-UOV 假设、多元密码分析与安全证明都未成熟；这些取舍多年后仍可作为协议设计参照。

**「什么时候再读」** 当你需要为匿名凭证、盲签名或 Privacy Pass 类协议评估后量子迁移时，可重读此文；尤其适合比较哈希求值主导的成本结构。注意参数与安全证明仍在变化，文中尺寸是 2026 年的阶段性估算。

**标签**: `#post-quantum cryptography`, `#privacy`, `#anonymous credentials`, `#blind signatures`, `#web protocols`

---

<a id="item-reading-4"></a>
### [OpenSSH 在 musl 无 PAM 环境下的锁定账户登录漏洞](https://sshhole.com/) ⭐️ 8.2/10

文章追溯 OpenSSH 在 musl 无 PAM 环境下的认证漏洞：crypt\(\) 失败返回“\*”，与 /etc/shadow 锁定账户的“\*”相撞，257 字节以上密码因此可能登录。

rss · Tildes · 11月6日 12:46 · 网页正文提取

**「为什么值得读」** 它把“哨兵值碰撞”讲成可复用的调试线索：crypt\(\) 失败返回“\*”，锁定账户也存“\*”，未走 PAM 的 sshd 又直接比较两者，超长密码可能因此跨过边界。作者用提交、CVE 和邮件列表串起几次接近发现的案例，提醒检查错误返回值，并按 libc/PAM 组合做矩阵测试；这些方法比单一漏洞更耐久。叙述带风格化处理，日期与结论宜当作待核实线索。

**「什么时候再读」** 审查 sshd/libc 认证路径、设计锁定字段，或排查 musl 与 PAM 组合的登录异常时再读；文章停在发现阶段，完整披露和修复进展需另查。

**标签**: `#security`, `#unix`, `#open-source`, `#debugging`, `#software-history`

---

