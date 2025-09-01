#app\oauth2.py
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from . import schemas,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET_KEY   密钥key
#Algorithm     算法
#Expriation time   过期时间

# 可以自定义设置，使用hello都行
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# 产生令牌
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire}) # 给to_encode增加一个字段
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

# 验证令牌，成功则返回用户的id字典
def verify_access_token(token:str,credentials_exception):
    try:
        paload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        userid = paload.get("user_id")
        # print(type(userid))
        # print("*:"*100,userid)
        if userid is None:
            raise credentials_exception
        
        token_data = schemas.TokenDate(id=userid)  # 只包含了用户id
       
    except JWTError:
        raise credentials_exception
    return token_data   # 返回是包含用户id的字典


# 获取用户信息    
def get_current_user(token:str=Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,detail="认证失败！",
        headers={"www-Authenticate":"Bearer"}
        )
    token = verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user  # 返回的是用户信息字典