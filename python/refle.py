#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select


engine = create_engine('sqlite:///test.db',echo =True)
metadata=MetaData()
meta=metadata

## auto reflect

meta.reflect(bind=engine)
users=meta.tables['users']
address=meta.tables['addresses']


##### test1
#users= Table('users',metadata,autoload=True,autoload_with=engine)

#for c in users.columns:
#    print c

s=select([users])
conn=engine.connect()
result=conn.execute(s)

for row in result:
    print "name is :" , row[users.c.name]
