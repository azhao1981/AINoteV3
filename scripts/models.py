import uuid
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 创建基类
Base = declarative_base()

# 定义 App 模型
class App(Base):
    __tablename__ = 'apps'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    
    # 定义与 Agent 的关系
    agents = relationship("Agent", back_populates="app")

# 定义 Agent 模型
class Agent(Base):
    __tablename__ = 'agents'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    app_id = Column(UUID(as_uuid=True), ForeignKey('apps.id'), nullable=False)
    
    # 定义与 App 的关系
    app = relationship("App", back_populates="agents")

# 数据库连接配置示例（请根据实际情况修改）
# DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建表（需要有效的数据库连接）
# Base.metadata.create_all(bind=engine)

# 获取数据库会话（需要有效的数据库连接）
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()