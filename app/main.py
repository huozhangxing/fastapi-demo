# app\main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware


# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
# models.Base.metadata.create_all(bind=engine) #有了alembic之后可以不使用这行，每次使用alembic创建数据库

app = FastAPI()

# origins = [
#     "https://www.baidu.com"
# ]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

