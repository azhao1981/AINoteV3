# tabiew

NOTE：这个效果看起来很炸啊
TODO：把这个+git key / search ,做成TIG，或crush做成Tig
https://github.com/awslabs/git-secrets aws 开源
https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/patterns/scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets.html
编译 | 如何扫描 GitHub 上所有「乌龙提交」以寻找泄露的密钥
https://zhuanlan.zhihu.com/p/1924131440066540628
从攻击视角看代码隐私安全，9款Git秘密扫描工具盘点
https://github.com/trufflesecurity/trufflehog
https://github.com/Yelp/detect-secrets

https://www.secrss.com/articles/40954
命令行数据文件可视化浏览工具。这是一款用于浏览和查询表格数据文件（如 CSV、Parquet、Arrow、Excel 等）的命令行工具。它提供交互式界面体验、支持 SQL 查询、多表操作、模糊搜索和 Vim 风格快捷键等功能。

https://github.com/shshemi/tabiew

https://img.hellogithub.com/i/n9ew6icrjGoHDxb_1753535564.gif

未分类

## 访问 git
```bash
git log main --author="Alice" -n 5 --oneline

git log develop --author="weiz" -n 10
git log master --author="weiz" -n 10

git log --author="Alice" -n 5
```

如何用MCP来实现在这个需求？
TODO: 这个怎么弄？下面的MCP都不怎么看得懂怎么跑

https://glama.ai/mcp/servers/@modelcontextprotocol/git
https://mcp.so/server/git-mcp-server
https://github.com/cyanheads/git-mcp-server 可是只有 100星

https://mcp.so/server/local-git-mcp-server/okdshin
Local Git MCP Server is a Python-based server that allows users to manage local Git repositories using the Message-based Communication Protocol (MCP).


https://github.com/KunihiroS/claude-code-mcp
这个是相关的吗？

https://apidog.com/blog/top-10-mcp-servers-for-git-tools/
  https://github.com/awslabs/mcp
  A suite of specialized MCP servers that help you get the most out of AWS, wherever you use MCP.


https://gitmcp.io/
Instantly create a Remote MCP server for any GitHub repository
Simply change the domain from github.com or github.io to gitmcp.io and get instant AI context for any GitHub repository.

https://github.com/github/github-mcp-server
GitHub's official MCP Server

A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.
https://github.com/adhikasp/mcp-git-ingest

