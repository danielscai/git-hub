#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///test1.db',echo =True)
Base=declarative_base()

class User(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True)
    name=Column(String)
    fullname=Column(String)
    password=Column(String)

    def __init__(self,name,fullname,password):
        self.name=name
        self.fullname=fullname
        self.password=password

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name,self.fullname,self.password)

Base.metadata.create_all(engine)

ed_user=User('dcai','Hello','edpassword')
print ed_user.name
print ed_user.password


Session=sessionmaker(bind=engine)
session=Session()
session.add(ed_user)


#our_user = session.query(User).filter_by(name='dcai').first()
query=session.query(User).filter(User.name.like('%dcai')).order_by(User.id)
print query.all()

#print user2
#print ed_user is our_user

#session.commit()

