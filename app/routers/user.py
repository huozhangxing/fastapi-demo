# app\routers\user.py
from typing import List
from fastapi import HTTPException,status,Depends,APIRouter
from .. import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["用户操作"],prefix="/users")
#**********users 表***********************
# 增加
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
async def create_user(user:schemas.CreateUser,db:Session= Depends(get_db)):
    # 将用户输入的密码计算出来hash值，并赋值给原来的位置
    hashed_password = utils.hash_pwd(user.password)
    user.password = hashed_password
    # $2b$12$Rp4rc0Gox4fHoJHpup3jCeQhD.hhDyOXQeAYiYcst9zP81jK5lxOq
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # 将提交的数据再写入到new_user中，相当于 sql语句中returning
    return new_user   # 返回数据包含了数据库中的所有字段信息

# 根据id查询用户
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.UserOut)
async def get_user(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到id为{id}的用户！")
    return user

# 查询所有用户
@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.UserOut])
async def get_users(db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到任何用户！")
    return users