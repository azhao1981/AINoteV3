
# 氛围编程 (vibe coding)

氛围编程 (vibe coding) 是一种新兴的软件开发实践，它使用人工智能 (AI) 根据自然语言提示生成功能代码，从而加快开发速度，并让应用构建变得更加容易，对于那些编程经验有限的用户尤其如此。

该术语由 AI 研究人员 Andrej Karpathy 于 2025 年初创造，用于描述一种工作流，其中开发者的主要角色从逐行编写代码转变为通过对话风格更浓的过程指导 AI 助理生成、完善和调试应用。这样，您就可以腾出时间和精力思考大方向或应用的主要目标，而 AI 则负责编写实际代码。
## MCP

https://github.com/modelcontextprotocol/servers

### playwright-mcp
https://github.com/microsoft/playwright-mcp

```bash
claude mcp add playwright npx @playwright/mcp@latest
# Added stdio MCP server playwright with command: npx @playwright/mcp@latest to local config
# File modified: /home/weiz/.claude.json [project: /home/weiz/projects/github.com/Claude-Code-Multi-Agent]
```

### memory
这个好像有点问题，并不能在这个页面里看到
https://memory.mcpgenerator.com/

https://github.com/puliczek/mcp-memory

```json
{
  "mcpServers": {
    "mcp-memory": {
      "url": "https://memory.mcpgenerator.com/b79369a1-4f32-4ca2-b621-4122d1db1296/sse"
    }
  }
}
```
 我找到了多个可用的memory MCP工具：

  1. @modelcontextprotocol/server-memory - 官方MCP memory服务器
  2. cf-memory-mcp - 高级内存管理工具
  3. memory-engineering-mcp - 企业级内存工程工具
  4. modular-mcp-memory - 模块化记忆系统
  5. @nova-mcp/mcp-nova - AI记忆系统

```bash
claude mcp add memory npx @modelcontextprotocol/server-memory
```

直接用：
在 .mcp.json 安装 mcp-feedback-enhanced browsermcp shrimp-task-manager  playwright-mcp  和 memory
  已安装的 MCP 服务器：

  1. ✅ sequential-thinking - 逐步思考工具
  2. ✅ mcp-feedback-enhanced - 增强型反馈工具
  3. ✅ browsermcp - 浏览器控制工具
  4. ✅ shrimp-task-manager - 任务管理工具
  5. ✅ playwright-mcp - Playwright 自动化测试工具
  6. ✅ memory - 记忆存储工具

  现在您的项目已经配置了完整的 MCP 服务器套件，包括：

  - 思考和分析工具：sequential-thinking
  - 交互反馈工具：mcp-feedback-enhanced
  - 浏览器自动化：browsermcp
  - 任务管理：shrimp-task-manager
  - Web 自动化测试：playwright-mcp
  - 记忆存储：memory

## 增强资源

### Claude-Code-Multi-Agent 开源发布，强大的claude code Subagent工作流

https://github.com/Prorise-cool/Claude-Code-Multi-Agent
> Context Engineering 驱动的新一代AI编程助手生态系统，基于Claude Code构建的智能代理协调平台，实现从需求到交付的全流程自动化开发
> fork: https://github.com/azhao1981/Claude-Code-Multi-Agent
>

```bash
git clone git@github.com:azhao1981/Claude-Code-Multi-Agent.git
```



### ccr

https://github.com/musistudio/claude-code-router/blob/main/README_zh.md

### roo-code
https://github.com/RooCodeInc/Roo-Code

### kilo

### BMad-Method: Universal AI Agent Framework
https://github.com/bmadcode/BMAD-METHOD 
智能体敏捷驱动开发（Agentic Agile Driven Development）是敏捷人工智能驱动开发的突破性方法，其基础和意义远不止于此。凭借专业的AI专长，赋能任何领域：从软件开发、娱乐、创意写作、商业策略到个人健康，仅举几例。




### 收集数据

一键将代码库转换为 AI 友好格式的工具。该项目可将任意 GitHub 仓库快速转换为适合大语言模型处理的纯文本摘要。使用起来十分方便，只需将 GitHub 项目地址中的 hub 替换为 ingest 即可得到文本摘要。
https://github.com/coderamp-labs/gitingest

https://gitingest.com/


Automate security reviews with Claude Code
https://telegra.ph/Automate-security-reviews-with-Claude-Code-08-06