#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(255))

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    posts = Column(String(5060), unique=True)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    