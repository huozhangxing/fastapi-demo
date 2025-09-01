# # app\schemas.py
from pydantic import BaseModel,EmailStr,Field
from datetime import datetime
from typing import Optional


# 使用BaseModel对post字段进行校验
class PostBase(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass



# 定义用户提交的注册的模型，做验证
class CreateUser(BaseModel):
    email:EmailStr   # 依赖模块email_validator==2.2.0 
    password:str
# 定义响应模型，不返回密码
class UserOut(BaseModel):
    id: int
    email:EmailStr
    create_at:datetime

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenDate(BaseModel):
    id:Optional[int] = None


# 定义响应数据模型（包含的都是返回给客户端的信息，不想返回的，可以去掉字段）
# 继承PostBase基类的所有字段，并且添加了2个字段
class ResponsePost(PostBase):
    id:int
    create_at:datetime
    owner_id:int        # 只返回用户id
    owner:UserOut    # 与models中的Post.owner relationship配合,可以返回用户的具体信息，id email create_at
    # class Config:
    #     orm_mode = True

#  {'type': 'missing', 'loc': ('response', 10, 'post'), 'msg': 'Field required', 'input': {'Post': <app.models.Post object at 0x00000277F73A5A30>, 'votes': 0}}
class ResponsePost1(BaseModel):
    Post:ResponsePost    #  pydantic 识别的字段就是Post  必须是这个
    votes:int


class Vote(BaseModel):
    post_id:int
    dir: int = Field(ge=0,le=1)  # 限制0和1  1是点赞  0 是取消点赞
