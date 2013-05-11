#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select


engine = create_engine('sqlite:///test.db',echo =True)

metadata=MetaData()
users= Table('users',metadata,
        Column('id',Integer,primary_key=True),
        Column('name',String),
        Column('fullname',String),
)

addresses=Table('addresses',metadata,
        Column('id',Integer,primary_key=True),
        Column('user_id',None,ForeignKey('users.id')),
        Column('email_address',String,nullable=False)
)


#metadata.create_all(engine)

conn=engine.connect()

with conn.begin() as trans:
    r1=conn.execute(select([users]))
    for row in r1:
        print row
