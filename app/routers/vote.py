# app\routers\vote.py
from fastapi import APIRouter,status,HTTPException,Depends
from .. import schemas,database,oauth2,models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/vote",tags=["点赞功能"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def vote(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:schemas.UserOut=Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    # 贴子不存在，则返回异常
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到id为{vote.post_id}的帖子，无法执行点赞相关操作！")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
   
    if (vote.dir == 1):
         # 点赞
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"id为{current_user.id}的用户已经对id为{vote.post_id}的文章点过赞,无法继续点赞")
        # 没找到点赞记录，进行点赞
        new_vote = models.Vote(post_id=post.id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":f"id为{current_user.id}的用户对id为{vote.post_id}的文章点赞一次。"}
    else:
        # 取消点赞
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到点赞记录。用户id是{current_user.id},帖子id是{post.id}")
        # 找到了点赞记录
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":f"对id是{post.id}的帖子取消点赞成功"}