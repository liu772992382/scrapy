#coding=utf-8
# 导入:
from sqlalchemy import Column, String, create_engine,MetaData,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 获取元数据
metadata = MetaData()
# 定义User对象:

class douban_movie(Base):
    __tablename__ = 'douban_movie'

    id = Column(Integer, primary_key = True)
    name = Column(String(300))
    rating_nums = Column(String(5))
    url = Column(String(500))


class douban_book(Base):
    # 表的名字:
    __tablename__ = 'douban_book'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    info = Column(String(200))
    rating_nums = Column(String(5))
    img_id = Column(String(500))


#知乎关注关系数据表
class zhihu_follow(Base):
    __tablename__ = 'zhihu_follow'

    id = Column(Integer,primary_key=True)
    user = Column(String(100))
    follower = Column(String(100))
    type = Column(Integer)  #关注关系，1代表user被关注，0代表follower被关注，2代表相互关注

    #def Insert(self,data):  #data为(user,follower)




# 初始化数据库连接:
engine = create_engine('mysql+mysqldb://root:19951028liu@localhost:3306/scrapy?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#创建从Base派生的所有表
def createAll(eng):
	Base.metadata.create_all(eng)
