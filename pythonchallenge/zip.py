#!/usr/bin/python


import re
import zipfile

init='90052'
cont=init

def get_next(file_name):
    path='/home/dcai/Downloads/1/'
    
    file1=open(path + file_name + '.txt')
    cont=file1.read()
    ret=re.findall(u'\D*Next nothing is (\d+)',cont)
    if ret:
        return ret[0]
    else:
        return False

file_path='/home/dcai/Downloads/channel.zip'

a=[]
with zipfile.ZipFile(file_path,'r') as myzip:
    while cont:
        zinfo=myzip.getinfo(cont+'.txt')
        a.append(zinfo.comment)
        cont=get_next(cont)

print ''.join(a)
