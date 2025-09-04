# app\models.py
from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
class Post(Base):
    # 指定表名
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,nullable=False,server_default='True') # 指定默认值是True
    # 帖子发布时间（带时区），默认是当前时间，不允许为空
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False) # users是表名字
    # relationship 也是依靠的外键，找到了帖子对应的用户的详细信息
    owner = relationship("User")   # 关联User表 与schemas中的ResponsePost.owner配合

class User(Base):
    __tablename__ = "users"
    # unique 设置邮箱不能重复
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    # sex = Column(String,nullable=False,server_default="")

class Vote(Base):
    __tablename__ = "votes"
    # 使用的是复合主键
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)