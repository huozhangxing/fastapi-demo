# app\utils.py
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

# 传入密码，得到密码的hash结果
def hash_pwd(pwd:str):
    return pwd_context.hash(pwd)

# 校验明文密码plain_password 和 hashed之后的hashed_password   看是否密码正确
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)