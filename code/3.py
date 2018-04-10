#!/usr/bin/env python 
#-*- coding:utf-8 -*-
#Author:PeterYJC(yjcpeter@gmail.com)

def isPerfectNum(n):
    a = 1 
    b = n
    s = 0

    while a < b:
        if b % a == 0:
            s += a + b 
        a += 1 
        b = n / a 
    
    if a == b and a * b == n:
        s += a 

    return s -n == n 

for i in range(2,10000):
    if isPerfectNum(i):
        print i 