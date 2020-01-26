from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class restaurant(Base):
   __tablename__ = 'restaurant'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   picture_link = Column(String)
   description = Column(String)

