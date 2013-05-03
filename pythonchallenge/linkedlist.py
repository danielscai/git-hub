#!/usr/bin/python

import urllib
import re


def get_next(url_sufix):
    url_base='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    res=urllib.urlopen(url_base+url_sufix)
    cont=res.read()
    print cont
    ret=re.findall(u'\D*next nothing is (\d+)',cont)
    return ret[0]


url_init='49574'
url=url_init


while url:
    ret=get_next(url)
    url=ret
