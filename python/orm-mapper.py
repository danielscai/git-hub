#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

engine = create_engine('sqlite:///mapper.db',echo =True)
metadata=MetaData()

user=Table('user',metadata,
        Column('id',Integer,primary_key=True),
        Column('name',String(50)),
        Column('fullname',String(50)),
        Column('password',String(12))
)

class User(object):
    def __init__(self,name,fullname,password):
        self.name=name
        self.fullname=fullname
        self.password=password

mapper(User,user)
