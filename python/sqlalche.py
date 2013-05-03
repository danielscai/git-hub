#!/usr/bin/python

from sqlalchemy.orm import mapper, sessionmaker

from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, Unicode, DateTime

engine = create_engine("sqlite:///tutorial.db", echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
            Column('id', Integer, primary_key=True),
                Column('name', String(50)),
                    Column('fullname', String(50)),
                        Column('password', String(100))
                        )
metadata.create_all(engine)

metadata = MetaData(engine)
users_table = Table('users', metadata, autoload=True)
print users_table.columns


insert =  users_table.insert()
insert.execute(name='leon', fullname='leon liang', password='leon123')
class User(object): pass
mapper(User, users_table)

ed_user=User('crackpot','Crackpot','password')
print 'username:', ed_user.name
print 'fullname:', ed_user.fullname
print 'password:', ed_user.password
print 'id:', str(ed_user.id)

