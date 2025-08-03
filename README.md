# 大模型企业级开发

## 1. 大模型基础理论
- 大语言模型 (LLM) 概述
- Transformer 架构详解
- 预训练与微调 (Pre-training & Fine-tuning)
- 提示工程 (Prompt Engineering)
- 大模型评估指标

## 2. 编程语言与高级技巧

### 2.1. 编程语言基础
- Python 基础语法与特性
- Go 基础语法与特性
- TypeScript/JavaScript 基础语法与特性
  - Node.js 与 pnpm 配置: `notes/node_pnpm.md`

#### Python 包管理与环境工具 (uv)

```shell
pip install uv -U
$env:UV_PYTHON_INSTALL_MIRROR = "https://gh-proxy.com/github.com/indygreg/python-build-standalone/releases/download"
uv python install 3.12
# Installed Python 3.12.11 in 34.52s
 + cpython-3.12.11-windows-x86_64-none (python3.12.exe)
# warning: `C:\Users\azhao\.local\bin` is not on your PATH. To use installed Python executables, run `$env:PATH = "C:`\Users`\azhao`\.local`\bin;$env:PATH"` or `uv python update-shell`.
uv python update-shell
# C:\Users\azhao\.local\bin
```

```bash
pip install uv -U
UV_PYTHON_INSTALL_MIRROR="https://gh-proxy.com/github.com/indygreg/python-build-standalone/releases/download" uv python install 3.12
```

### 2.2. 高级编程技巧

#### Python 高级技巧
- SQLAlchemy 解决 N+1 查询问题
  - 参考资料: `notebooks/sqlalchemy_n_plus_one学习.md`
- 异步编程 (asyncio)
- 装饰器与元类
- 性能分析与优化

#### Go 高级技巧
- 并发编程 (Goroutines & Channels)
- 接口与组合
- 内存管理与性能优化
- 错误处理最佳实践

#### TypeScript/JavaScript 高级技巧
- TypeScript 高级类型 (泛型, 条件类型等)
- 异步编程 (Promise, async/await)
- 模块系统与依赖管理
- Node.js 性能优化

## 3. 企业级开发核心技术

### 3.1. 检索增强生成 (RAG - Retrieval-Augmented Generation)
- RAG 基本概念与架构
- 向量数据库 (Vector Database)
- 倒数排名融合 (RRF) 在混合检索中的应用
  - 参考资料: `notes/RRF.md`
- 多路召回策略

### 3.2. 大模型应用框架
- LangChain 框架详解
- LlamaIndex 框架详解
- 自定义 Agent 设计与实现
- 工具调用 (Tool Calling) 与 Function Calling

### 3.3. 模型部署与服务化
- 模型量化与优化
- 使用 vLLM 部署大模型
- OpenAI API 兼容接口设计
- 微服务架构与容器化 (Docker, Kubernetes)

### 3.4. 性能监控与优化
- 模型推理性能分析
- 服务延迟与吞吐量优化
- 缓存策略 (Cache Strategy)
- 负载均衡与高可用

### 3.5. 代码生成与辅助工具
- 代码理解与生成
- 代码审查辅助
- 自动化测试生成
  - Qwen Code: `notes/qwen_code.md`

## 4. 企业级应用开发实践

### 4.1. 智能客服系统
- 对话系统设计
- 多轮对话管理
- 意图识别与实体抽取
- 知识库构建与更新

### 4.2. 智能文档处理平台
- 文档解析与信息提取
- 自动摘要生成
- 问答系统实现

### 4.3. 个性化推荐系统
- 用户画像构建
- 内容理解与表征
- 推荐算法与排序模型

## 5. 安全与合规
- 数据隐私与保护 (GDPR, CCPA)
- 模型安全与对抗攻击防护
- 内容安全审核
- 算法公平性与偏见消除

## 6. 项目管理与最佳实践
- 敏捷开发在 AI 项目中的应用
- 模型版本控制与实验管理 (MLflow)
- 持续集成与持续部署 (CI/CD) for AI
- 团队协作与沟通

## 7. 前沿技术与未来趋势
- 多模态大模型 (Multimodal LLM)
- 自主 Agent 与多 Agent 系统
- 联邦学习 (Federated Learning)
- 边缘计算与大模型