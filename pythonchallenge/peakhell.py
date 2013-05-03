#!/usr/bin/python

import pickle 


file1=open('banner.p')
pk=pickle.load(file1)


for i in pk:
    #print i
    print ''.join(map(lambda x: x[0]*x[1],i))
    #print (''.join(map(lambda x:x[0]* x[1],i)))

