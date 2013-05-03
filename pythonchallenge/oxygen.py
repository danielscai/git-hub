#!/usr/bin/python

import Image
import re


image=Image.open('oxygen.png')
data=image.convert('L').getdata()

message=[]
for i in range(4,608,7):
    message.append(chr(data[image.size[0]*50+i])) 

#print ''.join(message)

im=Image.open('oxygen.png')
#r,g,b=im.split()

#im=Image.merge('RGB',(b,g,r))
out=im.resize((128,128))
out=im.rotate(45)
out.save('hi.png')



