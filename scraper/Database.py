from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://ZeroDay:1234@0.0.0.0:5432/ZeroDayDB")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    type = Column(String)
    link = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
