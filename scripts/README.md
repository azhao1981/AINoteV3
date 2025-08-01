# 数据库配置示例

在运行 `scripts/query_examples.py` 之前，请确保你已经正确配置了数据库连接。

1. 安装 PostgreSQL 数据库并确保它正在运行。
2. 创建一个数据库，例如 `ainotev3`。
3. 创建一个数据库用户并授予相应的权限。
4. 修改 `scripts/models.py` 文件中的 `DATABASE_URL` 变量，将其更新为你的实际数据库连接信息：

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
```

5. 取消注释 `scripts/models.py` 和 `scripts/query_examples.py` 中的相关代码以启用数据库功能。

6. 运行 `scripts/query_examples.py` 来执行示例查询。

注意：请确保你的数据库服务器正在运行，并且防火墙规则允许应用程序连接到数据库端口（默认是 5432）。