#!/usr/bin/env python 
#-*- coding:utf-8 -*-
#Author:PeterYJC(yjcpeter@gmail.com)

l = range(10)
count = 0 

for a in l[1:]:
    for b in l:
        if a == b: continue
        for c in l:
                if c != a and c != b:
                    print a,b,c
                    count += 1 

print '总的个数是：',count             


