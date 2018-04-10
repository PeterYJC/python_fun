#!/usr/bin/env python 
#-*- coding:utf-8 -*-
#Author:PeterYJC(yjcpeter@gmail.com)

def isSXHNumber(n):
    a = []
    k = n 
    while k > 0:
        a.append(k % 10)
        k /= 10 
    
    j = len(a)
    return sum([x ** j for x in a]) == n 

for x in range(100,500):
    if isSXHNumber(x):
        print x 