

● 代码节点 (Code Node) 的实现主要分布在以下位置：

  后端实现

  - /api/core/workflow/nodes/code/code_node.py - 主要的代码节点实现
  - /api/core/workflow/nodes/code/entities.py - 数据模型和架构
  - /api/core/helper/code_executor/ - 代码执行引擎

  前端实现

  - /web/app/components/workflow/nodes/code/panel.tsx - 配置面板
  - /web/app/components/workflow/nodes/code/node.tsx - 节点组件
  - /web/app/components/workflow/nodes/code/use-config.ts - 配置钩子

  核心功能

  - 支持 Python3 和 JavaScript 执行
  - 沙箱化代码执行环境
  - 变量输入输出管理
  - 类型验证和错误处理
  - 依赖管理（仅 Python）