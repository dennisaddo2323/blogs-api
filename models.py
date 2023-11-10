from database import Base
from sqlalchemy import Column,String,Integer

class Details(Base):
    __tablename__='datails'
    id=Column(Integer,primary_key=True,index=True)
    lastname=Column(String)
    firstname=Column(String)
    email=Column(String)