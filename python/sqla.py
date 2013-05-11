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

#ins=users.insert().values(name='dcai1',fullname='daniels cai')
#ins.bind=engine
#str(ins)
#print ins.compile().params
#conn=engine.connect()
#result=conn.execute(ins)
#print result
#print result.inserted_primary_key

conn=engine.connect()
ins=users.insert()
#conn.execute(ins,name='dc',fullname='danx')


addr_ins=addresses.insert()

'''
res=conn.execute(addr_ins,[
    {'user_id':1,'email_address':'dcai@walmart.com'},
    {'user_id':1,'email_address':'hello@123.com'},
    {'user_id':2,'email_address':'helxxx@34.com'},
    {'user_id':2,'email_address':'helxfsdf@we.com'},
])

print res
'''

s=select([users,addresses]).where(users.c.id == addresses.c.user_id)
result=conn.execute(s)

for row in result:
    print row

#row=result.fetchone()

#print row
#print 'name:',row[1],',fullname:',row[2]
#print 'name:',row[users.c.name],',fullname:',row[users.c.fullname]


print users.c.name.like("d%")


result=conn.execute("select name from users")
for row in result:
    print "username",row[users.c.name]
