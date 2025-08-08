
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


## cc proxy
企业级的多渠道大模型 API 管理平台。这是一款用 Go 语言开发的企业级大模型接口管理平台，支持 OpenAI、Gemini、Claude 等多种服务。它开箱即用、内置 Web 管理界面、保留原生 API 格式，支持密钥自动轮询、故障切换和水平扩展，专为高并发生产环境而设计。
https://github.com/tbphp/gpt-load

https://github.com/1rgs/claude-code-proxy
https://github.com/CogAgent/claude-code-proxy
https://github.com/coffeegrind123/gemini-for-claude-code
https://github.com/musistudio/claude-code-router
https://github.com/BerriAI/litellm
https://github.com/chinrain/Api-Conversion

Toolify 是一个中间件代理，旨在为那些本身不支持函数调用功能的大型语言模型，或未提供函数调用功能的 OpenAI 接口注入兼容 OpenAI 格式的函数调用能力。它作为您的应用程序和上游 LLM API 之间的中介，负责注入必要的提示词并从模型的响应中解析工具调用。
https://github.com/funnycups/Toolify/blob/main/README_zh.md

https://github.com/UfoMiao/zcf
零配置，一键搞定 Claude Code 环境设置 - 支持中英文双语配置、智能代理系统和个性化 AI 助手
TODO： 这个不光是PROXY，大多数是用法，看下有哪些是要用的


一个能将多种大模型 API（Gemini, OpenAI, Claude...）统一封装为本地 OpenAI 兼容接口的强大代理。
AIClient2API：模拟Gemini CLI和Kiro 客户端请求，兼容OpenAI API。
可每日千次Gemini模型请求， 免费使用Kiro内置Claude模型。通过API轻松接入任何客户端，让AI开发更高效！
https://github.com/justlovemaki/AIClient-2-API


```bash
git clone git@github.com:azhao1981/gpt-load.git
git clone git@github.com:azhao1981/new-api.git
```
https://github.com/azhao1981/new-api 
Dify，当前仅支持chatflow
TODO: 真的支持 dify 了

[在 New API 使用 Claude Code 再也不用便秘poop了](https://linux.do/t/topic/852752)

看起来直接支持 CC 了

https://hub.docker.com/r/calciumion/new-api/tags

v0.8.8.6.0

```bash
docker pull calciumion/new-api:v0.8.8.6.0
```


