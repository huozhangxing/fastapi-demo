# app\database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

# 连接postgres数据库的url
# 数据库类型+驱动://用户名:密码@主机地址/数据库名
# url = "postgresql+psycopg2://postgres:123456@localhost:5432/fastapi"

url = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@\
{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# 创建引擎
engine = create_engine(url=url,echo=False)   # 会在控制台输出执行的 SQL 语句，便于调试，发布设置成false

# 创建数据库会话工厂
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# 创建 ORM 模型的基类
Base = declarative_base()

# 这是一个生成器函数，常用于 FastAPI 的依赖注入系统
# 为每个请求创建一个新的      数据库会话
# 使用 try/finally 确保会话在使用后正确关闭
# yield 将会话提供给请求处理函数使用
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
