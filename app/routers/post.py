# app\routers\post.py
from typing import List,Optional
from fastapi import HTTPException,status,Depends,Response,APIRouter
from .. import models,schemas,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func


router = APIRouter(tags=["帖子操作"],prefix="/posts")
#**********posts 表***********************
# 增加
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def create_post(post:schemas.PostCreate,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # get_current_user:models.User = Depends(oauth2.get_current_user) 设置需要认证
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(owner_id = get_current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return new_post   # 返回数据包含了数据库中的所有字段信息

# 删除
@router.delete("/{id}")
async def delete_post(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    if get_current_user.id != post.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"无权操作id为{id}的帖子")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK,content=f"id为{id}的帖子已经被删除！")

# 修改
@router.put("/{id}",response_model=schemas.ResponsePost)
async def update_post(id:int,post:schemas.PostCreate,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    will_update_post = post_query.first()
    if not will_update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    if get_current_user.id != will_update_post.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"无权操作id为{id}的帖子")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return will_update_post

# 查  查询所有内容
@router.get("/",response_model=List[schemas.ResponsePost1])
async def get_posts(db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user),
                      limit:int = 10,offset:int = 0,search_title:Optional[str]=""):
    # offset = 0  是第一页    skip 是跳过多少个 search是搜索关键字  url中%20代表空格
    # print(db.query(models.Post))  # 打印的是sql语句
    # print(get_current_user.email)

    
    # posts = db.query(models.Post).filter(models.Post.title.contains(search_title)).limit(limit).offset(offset*limit).all()    # 帖子公开
    # 用到了数据的左外连接
    res = db.query(models.Post,func.count(models.Vote.post_id).label("votes"))\
    .join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id)\
        .filter(models.Post.title.contains(search_title)).limit(limit).offset(offset*limit).all()
    # print(res)   # [(<app.models.Post object at 0x00000241FDC9C550>, 1)]
    new_res = [x._mapping for x in res]
    # _mapping 带上了属性名的字典，否则就是列表，不带属性名 [{'Post': <app.models.Post object at 0x000001A62414C550>, 'votes': 1}]

    # 帖子私有
    # posts = db.query(models.Post).filter(models.Post.owner_id == get_current_user.id).all()
    return new_res

@router.get("/{id}",response_model=schemas.ResponsePost1)
async def get_post(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # print(db.query(models.Post))
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    res = db.query(models.Post,func.count(models.Vote.post_id).label("votes"))\
    .join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id)\
        .filter(models.Post.id == id).first()
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    # 非公开，查询不是自己的id的帖子，也返回未找到的错误
    # if get_current_user.id != post.id:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"未找到id={id}的帖子!")
    return res._mapping