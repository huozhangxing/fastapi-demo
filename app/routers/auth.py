# app\routers\auth.py
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database,schemas,models,utils,oauth2

router = APIRouter(tags=["认证登录"])

# 用户登录的接口 OAuth2PasswordRequestForm 是让用户以表单的形式提交信息，这里面有2个字段 username 和 password 
@router.post('/login',response_model=schemas.Token)
async def login(login_user:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == login_user.username).first()
    # 未找到用户
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="用户名或者密码错误！")
    # 用户的密码不正确
    if not utils.verify(login_user.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="用户名或者密码错误！")
    # 密码正确，创建一个token，并返回给用户
    access_token =  oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}
    
    