# FastApi+PostgresSQL

## 初识FastApi

### 创建python虚拟环境

vscode创建python解释器的虚拟环境

在powershell中执行

```python
py -3 -m venv venv
```

![image-20250823162906762](FastApi+postgres.assets/image-20250823162906762.png)

### 选择python虚拟环境

查看-命令面板

![image-20250823163604181](FastApi+postgres.assets/image-20250823163604181.png)

![image-20250823163659264](FastApi+postgres.assets/image-20250823163659264.png)

### 激活虚拟环境

vscode的power shell 激活python的虚拟环境

```python
在vscode终端出现报错：无法加载文件\venv\Scripts\activate.ps1，因为在此系统上禁止运行脚本。

解决办法

1.vscode终端输入get-executionpolicy，回车返回Restricted。

2.复制Windows Powershall（window+X）在windows以管理员的身份运行，命令窗口输入set-executionpolicy remotesigned，回车，输入Y。

3.pycharm终端写入get-executionpolicy命令回车，返回remotesigned。

```

```python
激活命令
.\venv\Scripts\Activate.ps1 
```



### 安装FastApi

```python
# 激活环境后，在虚拟环境中安装FastApi
(venv) PS D:\Python\PyProject\FastApi_postgres> 
pip install fastapi[all] -i https://mirrors.aliyun.com/pypi/simple
# pip freeze 查看安装的环境  pip freeze > requirements.txt  可以输出到文件中
(venv) PS D:\Python\PyProject\FastApi_postgres> pip freeze
annotated-types==0.7.0
anyio==4.10.0
certifi==2025.8.3
click==8.2.1
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.116.1
fastapi-cli==0.0.8
fastapi-cloud-cli==0.1.5
h11==0.16.0
httpcore==1.0.9
httptools==0.6.4
httpx==0.28.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
markdown-it-py==4.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
orjson==3.11.2
pydantic==2.11.7
pydantic-extra-types==2.10.5
pydantic-settings==2.10.1
pydantic_core==2.33.2
Pygments==2.19.2
python-dotenv==1.1.1
python-multipart==0.0.20
PyYAML==6.0.2
rich==14.1.0
rich-toolkit==0.15.0
rignore==0.6.4
sentry-sdk==2.35.0
shellingham==1.5.4
sniffio==1.3.1
starlette==0.47.2
typer==0.16.1
typing-inspection==0.4.1
typing_extensions==4.14.1
ujson==5.11.0
urllib3==2.5.0
uvicorn==0.35.0
watchfiles==1.1.0
websockets==15.0.1
```

### 初次使用

```python
# main.py 
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world！"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

```python
#启动命令，在shell中执行
(venv) PS D:\Python\PyProject\FastApi_postgres> uvicorn app.main:app --reload 
INFO:     Will watch for changes in these directories: ['D:\\Python\\PyProject\\FastApi_postgres']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4824] using WatchFiles
INFO:     Started server process [10748]
INFO:     Waiting for application startup.
INFO:     Application startup complete.   
INFO:     127.0.0.1:61605 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:61605 - "GET /openapi.json HTTP/1.1" 200 OK
```

## PostgresSQL基础

```python
https://www.postgresql.org/download/
```

![image-20250825112819357](FastApi+postgres.assets/image-20250825112819357.png)

### 创建数据库

![image-20250825121532215](FastApi+postgres.assets/image-20250825121532215.png)

### 创建表

![image-20250825121452871](FastApi+postgres.assets/image-20250825121452871.png)

### 查询语句

![image-20250825122258033](FastApi+postgres.assets/image-20250825122258033.png)

```sql
# 查询表中的所有内容
select * from products;
# 只查看表中的某些字段
select id,name from products;
# 给字段重命名
select id as 商品id,name as 商品名称 from products;
# where关键字
select * from products where id = 5;   # 查看id等于5的记录 其他表达式  = >  <   >=  <=   != 
select * from products where id <> 5;    # != 和 <> 等价，都是查看id不等于5的数据
select * from products where id != 5;

# and关键字和or关键字
select * from products where id > 2 and price > 40 ;
select * from products where id < 2 or price > 40 ;

# in关键字
select * from products where id in (1,3,5);  #查看 id在（）中的记录
# like关键字
select * from products where name like '%TV%';  # 查看name中包含TV的
select * from products where name like 'TV%';  # 查看name中以TV开头的
select * from products where name like '%TV';	# 查看name中以TV结尾的

select * from products where name not like '%TV%';   # 查看name中不包含TV的记录
# oder by 排序  默认是asc 升序     desc降序
select * from products order by price asc;
select * from products order by price desc;

# 先按照库存inventory进行降序排，若inventory相同，则相同的内容按照pirce进行升序排（不写asc，默认就是）
select * from products order by inventory desc,price;

# 对id大于3的  按照price进行降序排列
select * from products where id > 3 order by price desc;

# limit关键字
select * from products limit 2;   # 只要2个
select * from products where price > 10 order by price  limit 2;

# offset关键字  偏移量，前3个不取，从第4个开始取2个，取出来的是4和5
select * from products order by id limit 2 offset 3;

```

### 插入语句

```sql
insert into products (name,price) values ('新能源汽车','10000');
```



```sql
#一次插入多条数据，并使用returning返回添加的所有字段信息

insert into products (name,price) values ('电脑','2000'),('手机','2500'),('平板','1500') returning *;
```

![image-20250825125713528](FastApi+postgres.assets/image-20250825125713528.png)

```sql
# 插入成功后返回想要的字段内容
insert into products (name,price) values ('computer','2000'),('phone','2500'),('pad','1500') returning name,is_sale,create_at;
```

![image-20250825125848765](FastApi+postgres.assets/image-20250825125848765.png)

### 删除语句

```sql
delete from products where id=10;
delete from products where id=10 returning *;
```

### 更新语句

```sql
update products set name = 'super car',price=99999 where id = 6 returning *;
```

## sql语句操作PostgresSQL

### pg创建posts表

```sql
CREATE TABLE public.posts
(
    id serial,
    title character varying NOT NULL,
    content character varying NOT NULL,
    published boolean NOT NULL DEFAULT True,
    create_at time with time zone NOT NULL DEFAULT now(),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.posts
    OWNER to postgres;
```

![image-20250826132645206](FastApi+postgres.assets/image-20250826132645206.png)

### 安装psycopy2库

```
在Python中，使用PostgreSQL数据库最常用的库是psycopg2
pip install psycopg2-binary -i https://mirrors.aliyun.com/pypi/simple
```

### 使用sql语句操作数据库

```python
import time
from typing import Union
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# 使用BaseModel对post字段进行校验
class Post(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True

# 连接数据库，若连接不上，每2秒重新连接一次，连接上就退出循环
while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            port='5432',
            database='fastapi',
            user='postgres',
            password="1234567",
            cursor_factory=RealDictCursor,  # 返回的sql结果包含了字段名的字典，否则只有值的列表
        )
        cursor = conn.cursor()
        print("连接数据库成功！")
        break
    except Exception as e:
        # 这里报错的内容不是我们想要的，解决办法就是修改数据库的配置文件
        # 数据库连接失败： 
        # 'utf-8' codec can't decode byte 0xd6 in position 67: invalid continuation byte
        # 若要实现正确打印出sql服务器返回的错误，需要修改postgresql.conf配置文件配置
        print("数据库连接失败：",e)
        time.sleep(2)

# 增,
# HTTP 201 Created 是一个成功的状态响应码，
# 表明请求已成功被服务器处理，并且服务器因此创建了一个或多个新的资源
@app.post("/posts",status_code=status.HTTP_201_CREATED)
async def insert_post(post:Post):
    cursor.execute(
        #f"""insert into posts (title,content,published) values({post.title},{post.content},{post.published})"""
        # 注意：不要是使用上面的形式，会出现sql注入的安全问题
        # 假设用户把 post.title = "''); DROP TABLE posts; --"
        # insert into posts (title,content,published) values(''); DROP TABLE posts; --,{post.content},{post.published})
        """insert into posts (title,content,published) values (%s,%s,%s) returning *""",
        (post.title,post.content,post.published)
        )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data":new_post}

# 删
@app.delete("/posts/{id}")
async def delete_post(id:int):
    cursor.execute("""delete from posts where id =%s  returning *""",str(id))
    del_post = cursor.fetchone()
    if not del_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子")
    conn.commit()
    return {"data":del_post}

# 改
@app.put("/posts/{id}")
async def update_post(id:int,post:Post):
    cursor.execute("""update posts set title=%s,content=%s,published=%s where id=%s returning *""",
                   (post.title,post.content,post.published,str(id)))
    update_post = cursor.fetchone()
    if not update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子")
    conn.commit()
    return {"data":update_post}

# 查（所有内容）
@app.get("/posts")
async def get_posts():
    cursor.execute("""select * from posts""")
    posts = cursor.fetchall()
    return {"data":posts}

# 查（根据id查找某一篇帖子）
@app.get("/posts/{id}")
async def get_post(id:int):
    cursor.execute("""select * from posts where id = %s""",str(id))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子")
    return {"data":post}
```

windows修改配置方法：

```python
# D:\program\PostgresSQL\data\postgresql.conf 的最后添加以下内容

datestyle = 'iso, mdy'
timezone = 'Asia/Shanghai'
lc_messages = 'en_US.UTF-8'                   # 区域设置用于消息
lc_monetary = 'en_US.UTF-8'                   # 区域设置用于货币格式
lc_numeric = 'en_US.UTF-8'                    # 区域设置用于数字格式
lc_time = 'en_US.UTF-8'                       # 区域设置用于时间格式

# 默认的客户端编码，这个是解决的配置
client_encoding = 'utf8'

# 这些设置可以在运行时被客户端改变
# 所以在这里设置的是服务器默认值
```

## ORM

```python
# sqlmodel依赖psycopg2-binary
pip install sqlalchemy -i https://mirrors.aliyun.com/pypi/simple

##
#SQLAlchemy==2.0.43
#sqlmodel==0.0.24   他是基于SQLAlchemy和pydantic
```

### sqlalchemy的原始sql语句的用法

```python
# app\database.py
# sqlalchemy的原始sql语句的用法（不用看这部分内容）
import sqlalchemy
from sqlalchemy import create_engine


# "postgres://<user>:<pwd>@<host>/databsename"
url = "postgresql+psycopg2://postgres:123456@localhost/fastapi"
engine = create_engine(url=url,echo=False)   # echo 打印信息，帮助调试，发布设置成false
conn = engine.connect()

# 使用最原始的sql语句进行查询
query = sqlalchemy.text("select * from posts")

res = conn.execute(query)
for i in res:
    print(i)

conn.close()
engine.dispose()
```

### sqlalchemy项目中实际使用方法

```python
# app\database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 连接postgres数据库的url
# 数据库类型+驱动://用户名:密码@主机地址/数据库名
url = "postgresql+psycopg2://postgres:123456@localhost/fastapi"

# 创建引擎
engine = create_engine(url=url,echo=True)   # 会在控制台输出执行的 SQL 语句，便于调试，发布设置成false

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
```

```python
# app\models.py
from .database import Base
from sqlalchemy import Column,Integer,String,Boolean
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
```

```python
# app\main.py
import time
from typing import Union
from fastapi import FastAPI,HTTPException,status,Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine,get_db
from sqlalchemy.orm import Session

# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 使用BaseModel对post字段进行校验
class Post(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True


@app.get("/sqlalchemy")
async def test_post(db:Session = Depends(get_db)):
    return {"status":"success"}
```

使用sqlalchemy实现数据库的增删改查

```python
import time
from typing import Union
from fastapi import FastAPI,HTTPException,status,Depends,Response
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine,get_db
from sqlalchemy.orm import Session

# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 使用BaseModel对post字段进行校验
class Post(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True

# *******************以下使用sqlalchemy对数据库进行增删改查************************
# 增加
@app.post("/sqlalchemy/posts",status_code=status.HTTP_201_CREATED)
async def sqlalchemy_insert_post(post:Post,db:Session= Depends(get_db)):
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return {"data":new_post}   # 返回数据包含了数据库中的所有字段信息

# 删除
@app.delete("/sqlalchemy/posts/{id}",status_code=status.HTTP_200_OK)
async def sqlalchemy_delete_post(id:int,db:Session= Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post.delete(synchronize_session=False)
    db.commit()
    return {"data":f"id为{id}的帖子已被删除！"}

# 修改
@app.put("/sqlalchemy/posts/{id}")
async def sqlalchemy_update_post(id:int,post:Post,db:Session= Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    will_update_post = post_query.first()
    if not will_update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return {"res":f"id为{id}的帖子已被更新！","data":will_update_post}

# 查  查询所有内容
@app.get("/sqlalchemy/posts")
async def sqlalchemy_get_posts(db:Session= Depends(get_db)):
    # print(db.query(models.Post))  # 打印的是sql语句
    posts = db.query(models.Post).all()
    return {"data":posts}

@app.get("/sqlalchemy/posts/{id}")
async def sqlalchemy_get_post(id:int,db:Session= Depends(get_db)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    return {"data":post}
```

### 将验证类独立到单独的文件

```python
# app\schemas.py
from pydantic import BaseModel
from datetime import datetime

# 使用BaseModel对post字段进行校验
class PostBase(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

# 定义响应数据模型（包含的都是返回给客户端的信息，不想返回的，可以去掉字段）
# 继承PostBase基类的所有字段，并且添加了2个字段
class ResponsePost(PostBase):
    id:int
    create_at:datetime
```

```PYTHON
# app\main.py
from typing import List
from fastapi import FastAPI,HTTPException,status,Depends,Response

from . import models,schemas
from .database import engine,get_db
from sqlalchemy.orm import Session

# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#**********posts 表***********************
# 增加
@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def insert_post(post:schemas.PostCreate,db:Session= Depends(get_db)):
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return new_post   # 返回数据包含了数据库中的所有字段信息

# 删除
@app.delete("/posts/{id}")
async def delete_post(id:int,db:Session= Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK,content=f"id为{id}的帖子已经被删除！")

# 修改
@app.put("/posts/{id}",response_model=schemas.ResponsePost)
async def update_post(id:int,post:schemas.PostCreate,db:Session= Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    will_update_post = post_query.first()
    if not will_update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return will_update_post

# 查  查询所有内容
@app.get("/posts",response_model=List[schemas.ResponsePost])
async def get_posts(db:Session= Depends(get_db)):
    # print(db.query(models.Post))  # 打印的是sql语句
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts/{id}",response_model=schemas.ResponsePost)
async def get_post(id:int,db:Session= Depends(get_db)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    return post
```

### 创建用户表

```python
# app\models.py
from .database import Base
from sqlalchemy import Column,Integer,String,Boolean
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

class User(Base):
    __tablename__ = "users"
    # unique 设置邮箱不能重复
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

```

```python
# # app\schemas.py
from pydantic import BaseModel,EmailStr
from datetime import datetime

# 使用BaseModel对post字段进行校验
class PostBase(BaseModel):
    # 帖子的id和创建时间create_at由数据库自己生成
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

# 定义响应数据模型（包含的都是返回给客户端的信息，不想返回的，可以去掉字段）
# 继承PostBase基类的所有字段，并且添加了2个字段
class ResponsePost(PostBase):
    id:int
    create_at:datetime

# 定义用户提交的注册的模型，做验证
class CreateUser(BaseModel):
    email:EmailStr   # 依赖模块email_validator==2.2.0 
    password:str
# 定义响应模型，不返回密码
class UserOut(BaseModel):
    id: int
    email:EmailStr
    create_at:datetime
```



```python
#**********users 表***********************
# 增加
@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
async def create_user(user:schemas.CreateUser,db:Session= Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # 将提交的数据再写入到new_user中，相当于 sql语句中returning
    return new_user   # 返回数据包含了数据库中的所有字段信息# app\main.py
from typing import List
from fastapi import FastAPI,HTTPException,status,Depends,Response

from . import models,schemas
from .database import engine,get_db
from sqlalchemy.orm import Session

# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#**********posts 表***********************
# 增加
@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def insert_post(post:schemas.PostCreate,db:Session= Depends(get_db)):
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return new_post   # 返回数据包含了数据库中的所有字段信息

# 删除
@app.delete("/posts/{id}")
async def delete_post(id:int,db:Session= Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK,content=f"id为{id}的帖子已经被删除！")

# 修改
@app.put("/posts/{id}",response_model=schemas.ResponsePost)
async def update_post(id:int,post:schemas.PostCreate,db:Session= Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    will_update_post = post_query.first()
    if not will_update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return will_update_post

# 查  查询所有内容
@app.get("/posts",response_model=List[schemas.ResponsePost])
async def get_posts(db:Session= Depends(get_db)):
    # print(db.query(models.Post))  # 打印的是sql语句
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts/{id}",response_model=schemas.ResponsePost)
async def get_post(id:int,db:Session= Depends(get_db)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    return post

#**********users 表***********************
# 增加
@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
async def create_user(user:schemas.CreateUser,db:Session= Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # 将提交的数据再写入到new_user中，相当于 sql语句中returning
    return new_user   # 返回数据包含了数据库中的所有字段信息
```

### 密码在数据库中的存储方式-hash值

```python
pip install passlib[bcrypt] -i https://mirrors.aliyun.com/pypi/simple
```

```python
# app\utils.py
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_pwd(pwd:str):
    return pwd_context.hash(pwd)
```

## 路由分发

```python
# app\main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user

# 根据模型定义创建数据库表
# 它会读取你通过 SQLAlchemy 模型类（继承自 Base）定义的所有表结构，然后在数据库中实际创建这些表。
# 如果存在该表，则不会再创建
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
```

```python
# app\routers\post.py
from typing import List
from fastapi import HTTPException,status,Depends,Response,APIRouter
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["1、帖子操作"],prefix="/posts")
#**********posts 表***********************
# 增加
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def insert_post(post:schemas.PostCreate,db:Session= Depends(get_db)):
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return new_post   # 返回数据包含了数据库中的所有字段信息

# 删除
@router.delete("/{id}")
async def delete_post(id:int,db:Session= Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK,content=f"id为{id}的帖子已经被删除！")

# 修改
@router.put("/{id}",response_model=schemas.ResponsePost)
async def update_post(id:int,post:schemas.PostCreate,db:Session= Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    will_update_post = post_query.first()
    if not will_update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return will_update_post

# 查  查询所有内容
@router.get("/",response_model=List[schemas.ResponsePost])
async def get_posts(db:Session= Depends(get_db)):
    # print(db.query(models.Post))  # 打印的是sql语句
    posts = db.query(models.Post).all()
    return posts

@router.get("/{id}",response_model=schemas.ResponsePost)
async def get_post(id:int,db:Session= Depends(get_db)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    return post
```

```python
# app\routers\user.py
from typing import List
from fastapi import HTTPException,status,Depends,APIRouter
from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["2、用户操作"],prefix="/users")
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
async def get_user(id:int,db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到id为{id}的用户！")
    return user

# 查询所有用户
@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.UserOut])
async def get_users(db:Session= Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"未找到任何用户！")
    return users
```

## 用户认证jwt

```python
jwt需要安装
pip install python-jose[cryptography]  -i https://mirrors.aliyun.com/pypi/simple
```

```python
# app\utils.py
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

# 传入密码，得到密码的hash结果
def hash_pwd(pwd:str):
    return pwd_context.hash(pwd)

# 校验明文密码plain_password 和 hashed之后的hashed_password   看是否密码正确
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
```

```python
# # app\schemas.py
from pydantic import BaseModel,EmailStr
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

# 定义响应数据模型（包含的都是返回给客户端的信息，不想返回的，可以去掉字段）
# 继承PostBase基类的所有字段，并且添加了2个字段
class ResponsePost(PostBase):
    id:int
    create_at:datetime

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
```

```python
#app\oauth2.py
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from . import schemas,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET_KEY   密钥key
#Algorithm     算法
#Expriation time   过期时间

# 可以自定义设置，使用hello都行
SECRET_KEY = "RVJgQn1n8woyDQg0FRrOnrJVk7RoUk9_nzR1GObhHbE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

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
```

```python
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
```

```python
# app\routers\post.py
from typing import List
from fastapi import HTTPException,status,Depends,Response,APIRouter
from .. import models,schemas,oauth2
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(tags=["帖子操作"],prefix="/posts")
#**********posts 表***********************
# 增加
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def create_post(post:schemas.PostCreate,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # get_current_user:models.User = Depends(oauth2.get_current_user) 设置需要认证
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # 将提交的数据再写入到new_post中，相当于 sql语句中returning
    return new_post   # 返回数据包含了数据库中的所有字段信息

# 删除
@router.delete("/{id}")
async def delete_post(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    post.delete(synchronize_session=False)
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
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(will_update_post)
    return will_update_post

# 查  查询所有内容
@router.get("/",response_model=List[schemas.ResponsePost])
async def get_posts(db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # print(db.query(models.Post))  # 打印的是sql语句
    # print(get_current_user.email)
    posts = db.query(models.Post).all()
    return posts

@router.get("/{id}",response_model=schemas.ResponsePost)
async def get_post(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    return post
```

## post表增加字段

```python
# app\routers\post.py
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
```

```python
# app\schemas.py
class ResponsePost(PostBase):
    id:int
    create_at:datetime
    owner_id:int        # 只返回用户id
    owner:UserOut    # 与models中的Post.owner relationship配合,可以返回用户的具体信息，id email create_at
```

根据登录用户身份，设置post的操作权限

```python
# app\routers\post.py
from typing import List,Optional
from fastapi import HTTPException,status,Depends,Response,APIRouter
from .. import models,schemas,oauth2
from ..database import get_db
from sqlalchemy.orm import Session


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
@router.get("/",response_model=List[schemas.ResponsePost])
async def get_posts(db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user),
                      limit:int = 10,offset:int = 0,search_title:Optional[str]=""):
    # offset = 0  是第一页    skip 是跳过多少个 search是搜索关键字  url中%20代表空格
    # print(db.query(models.Post))  # 打印的是sql语句
    # print(get_current_user.email)
    posts = db.query(models.Post).filter(models.Post.title.contains(search_title)).limit(limit).offset(offset*limit).all()    # 帖子公开
    # 帖子私有
    # posts = db.query(models.Post).filter(models.Post.owner_id == get_current_user.id).all()
    return posts

@router.get("/{id}",response_model=schemas.ResponsePost)
async def get_post(id:int,db:Session= Depends(get_db),
                      get_current_user:models.User = Depends(oauth2.get_current_user)):
    # print(db.query(models.Post))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"未找到id={id}的帖子!")
    # 非公开，查询不是自己的id的帖子，也返回未找到的错误
    # if get_current_user.id != post.id:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"未找到id={id}的帖子!")
    return post

```

## 添加配置文件

```python
# .env
# 数据库相关参数
DATABASE_HOSTNAME=127.0.0.1
DATABASE_PORT=5432
DATABASE_PASSWORD=123456
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres

# 认证相关配置
# 密钥key
SECRET_KEY=RVJgQn1n8woyDQg0FRrOnrJVk7RoUk9_nzR1GObhHbE
# 认证算法
ALGORITHM=HS256
# token有效期
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

```python
# app\config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    
    class Config:
        env_file=".env"

settings = Settings()

```

引用配置文件

```python
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
```

设置git提交忽略文件

```python
# .gitignore
__pycache__
venv/
.env

```

## 添加点赞功能

```python
# app\models.py
from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
class Vote(Base):
    __tablename__ = "votes"
    # 使用的是复合主键
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
```

```python
# # app\schemas.py
from pydantic import BaseModel,EmailStr,Field
from datetime import datetime
from typing import Optional

class Vote(BaseModel):
    post_id:int
    dir: int = Field(ge=0,le=1)  # 限制0和1  1是点赞  0 是取消点赞

```

```python
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
```

## 查询的帖子回复中增加点赞数

```python
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

```

```python
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
    print(type(db.query())) 
    print(hasattr(db.query(), 'mappings'))
    
    # posts = db.query(models.Post).filter(models.Post.title.contains(search_title)).limit(limit).offset(offset*limit).all()    # 帖子公开
    # 用到了数据的左外连接
    res = db.query(models.Post,func.count(models.Vote.post_id).label("votes"))\
    .join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id)\
        .filter(models.Post.title.contains(search_title)).limit(limit).offset(offset*limit).all()
    print(res)   # [(<app.models.Post object at 0x00000241FDC9C550>, 1)]
    new_res = [x._mapping for x in res]
    # _mapping 带上了属性名的字典，否则就是列表，不带属性名 [{'Post': <app.models.Post object at 0x000001A62414C550>, 'votes': 1}]
    print(new_res)
    print(type(new_res))
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
```

## 数据库迁移工具

```python
pip install alembic -i https://mirrors.aliyun.com/pypi/simple
```

```python
alembic init alembic  # 初始化
```

配置数据库连接信息alembic.ini，添加到这里容易泄露个人信息

```
# alembic.ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```

选择配置文件的方式，

```python
# alembic\env.py   # 只展示了部分代码
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app.config import settings

# from app.database import Base
from app.models import Base  # 这里一定是models中的base  不可以是database中的
target_metadata = Base.metadata  #导入模型，并设置 target_metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# 设置数据库连接url信息，使用配置文件的方式
config.set_main_option(
    "sqlalchemy.url",f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@\
{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
```

迁移方法

```python
# 第一次提交，会对当前的sqlchemy的models字段和数据库中的对比，因为内容一致，所以脚本中没有升级和回滚的操作
alembic revision --autogenerate -m "第一次使用alembic自动检测模型变化并生成迁移脚本"
alembic upgrade head   # 但是页要升级到对应的版本
```

```
#
class User(Base):
    __tablename__ = "users"
    # unique 设置邮箱不能重复
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    sex = Column(String,nullable=False,server_default="")
```

```python
#     
alembic revision --autogenerate -m "user表新增sex字段" 
alembic upgrade head 
```

```python
# 其他命令
alembic -h
alembic history
alembic current
alembic upgrade +1   # 升级到高一级版本
alembic downgrade -1  # 回滚到上一个版本
alembic upgrade <revision>  更新到指定版本
alembic downgrade base  回滚到初始状态，没有upgrade之前
alembic upgrade head  # 升级到最新版本
```

## 中间件

```python
fetch('http://127.0.0.1:8000/posts').then(res => res.json()).then(console.log)
```

![image-20250901141406043](FastApi+postgres.assets/image-20250901141406043.png)

出现跨域访问问题，解决办法是使用中间件

```python
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
```

使用中间件可以解决跨域问题。

![image-20250901141525468](FastApi+postgres.assets/image-20250901141525468.png)



## 使用git

github创建代码仓库返回的命令

```python
# …or create a new repository on the command line
echo "# fastapi-demo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/huozhangxing/fastapi-demo.git
git push -u origin main
```

```python
# …or push an existing repository from the command line
git remote add origin https://github.com/huozhangxing/fastapi-demo.git
git branch -M main
git push -u origin main
```

使用git将当前的代码提交代码库

```python
# .gitignore
__pycache__
venv/
.env
```

```python
配置git的账号和用户名
  git config --global user.email "huozhangxing@163.com"
  git config --global user.name "huozhangxing"

echo "# fastapi-demo" >> README.md
git init
git add --all
git commit -m "first commit"   # 若未配置git的账号和用户名会提示进行配置
git branch -m main         #git客户端默认是master分支，将当前的master分支重命名为main分支  -m等同于-M
git remote add origin https://github.com/huozhangxing/fastapi-demo.git  # 将远程仓库命名为origin
git push -u origin main
```

