

##  dify plugin init

1. Tools (工具)
      * Enabled: [✔]: 表示这个插件可以定义和使用自定义工具（Functions）。工具通常是执行特定任务的代码，比如调用外部API、进行计算或处理数据。启
        用后，插件就可以在Dify应用中提供这些功能。

2. Models (模型)
    * Enabled: [✘]: 表示这个插件本身不能直接调用Dify平台上的模型服务。如果启用，插件可以访问平台管理的模型。
    * LLM: [✘]: 表示不能调用大语言模型（如GPT、Claude等）。如果启用，插件可以直接与这些模型交互。
    * Text Embedding: [✘]: 表示不能调用文本嵌入模型。如果启用，插件可以将文本转换为向量表示。
    * Rerank: [✘]: 表示不能调用重排序模型。如果启用，插件可以对搜索或检索结果进行重新排序。
    * TTS: [✘]: 表示不能调用文本转语音模型。如果启用，插件可以将文本合成为语音。
    * Speech2Text: [✘]: 表示不能调用语音转文本模型。如果启用，插件可以将语音转换为文本。
    * Moderation: [✘]: 表示不能调用内容 moderation 模型。如果启用，插件可以检查内容是否符合特定标准（如安全性、 appropriateness）。

3. Apps (应用)
    * Enabled: [✘]:
      表示这个插件不能直接调用其他Dify应用（如BasicChat、ChatFlow、Agent、Workflow等）。如果启用，插件可以触发或与这些应用进行交互。

4. Resources (资源) / Storage (存储)
    * Storage Enabled: [✘]: 表示这个插件没有启用持久化存储功能。如果启用，插件可以存储数据（例如配置、缓存或用户数据）。
    * Size: N/A: 由于存储未启用，因此最大存储大小不适用（Not Applicable）。

5. Endpoints (端点)
    * Enabled: [✘]: 表示这个插件不能注册HTTP端点（API接口）。如果启用，插件可以对外提供Web服务，接收来自外部的请求。




这个看下是不是能参考一下
https://github.com/aws-samples/dify-aws-tool?tab=readme-ov-file
这个里面是DSL

https://github.com/svcvit/dify_plugin_collection
这是 DIFY 的官方市场 https://marketplace.dify.ai/ 插件安装包，方便离线用户自由选择。
如果你想开发一个插件，也可以将 .difypkg 修改为 .zip，直接解压，就可以看到源码。
TODO：看一下里面的JINA RERANK应该可以直接改来用

这个很不错
这个老哥是原dify的核心人员，好像是做sandbox的，还开源了一个兼容官方的sandbox
https://github.com/svcvit/Awesome-Dify-Workflow

https://github.com/svcvit/dify-sandbox-py/blob/main/README_CN.md

https://github.com/azhao1981/dify-sandbox-py

做为不开源部分的开源

https://dify101.com/