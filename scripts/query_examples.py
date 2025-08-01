import uuid
from sqlalchemy.orm import sessionmaker, joinedload, selectinload
from sqlalchemy import create_engine
from scripts.models import App, Agent

# 注意：此脚本需要有效的数据库连接才能运行
# 请确保你已正确配置数据库连接信息并取消注释相关代码

# # 数据库连接配置
# DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

def query_apps_with_agents_joinedload():
    """使用 joinedload 查询 apps 及其关联的 agents"""
    # apps_with_agents = session.query(App).options(joinedload(App.agents)).all()
    # for app in apps_with_agents:
    #     print(f"App: {app.name} ({app.id})")
    #     for agent in app.agents:
    #         print(f"  Agent: {agent.name} ({agent.id})")
    pass

def query_apps_with_agents_selectinload():
    """使用 selectinload 查询 apps 及其关联的 agents"""
    # apps_with_agents = session.query(App).options(selectinload(App.agents)).all()
    # for app in apps_with_agents:
    #     print(f"App: {app.name} ({app.id})")
    #     for agent in app.agents:
    #         print(f"  Agent: {agent.name} ({agent.id})")
    pass

def query_agents_with_app_joinedload():
    """使用 joinedload 查询 agents 及其关联的 app"""
    # agents_with_app = session.query(Agent).options(joinedload(Agent.app)).all()
    # for agent in agents_with_app:
    #     print(f"Agent: {agent.name} ({agent.id})")
    #     print(f"  App: {agent.app.name} ({agent.app.id})")
    pass

def query_agents_with_app_selectinload():
    """使用 selectinload 查询 agents 及其关联的 app"""
    # agents_with_app = session.query(Agent).options(selectinload(Agent.app)).all()
    # for agent in agents_with_app:
    #     print(f"Agent: {agent.name} ({agent.id})")
    #     print(f"  App: {agent.app.name} ({agent.app.id})")
    pass

if __name__ == "__main__":
    # 示例查询
    print("请确保数据库连接已正确配置，然后取消注释相关代码以运行查询。")
    # print("Querying apps with agents using joinedload:")
    # query_apps_with_agents_joinedload()
    
    # print("\nQuerying apps with agents using selectinload:")
    # query_apps_with_agents_selectinload()
    
    # print("\nQuerying agents with app using joinedload:")
    # query_agents_with_app_joinedload()
    
    # print("\nQuerying agents with app using selectinload:")
    # query_agents_with_app_selectinload()