#!/usr/bin/python

def qsort(L):
    if L==[]: return  []
    small=filter(lambda x:x<=L[0], L[1:])
    large=filter(lambda x:x>L[0],L[1:])
    return qsort(small) + L[0:1] + qsort(large)

print qsort([3,4,0,4,6,8,3,2,2])

