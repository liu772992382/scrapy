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
class douban_book(Base):
    # 表的名字:
    __tablename__ = 'douban_book'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    info = Column(String(200))
    rating_nums = Column(String(5))

# 初始化数据库连接:
engine = create_engine('mysql+mysqldb://root:19951028liu@localhost:3306/scrapy?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#创建从Base派生的所有表
def createAll(eng):
	Base.metadata.create_all(eng)
