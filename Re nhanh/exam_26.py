# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:50:00 2024

@author: 
"""
a= int(input("Nhập số a:  "))
b= int(input("Nhập số b:  "))
c= int(input("Nhập số c:  "))
x=0
if a>b:
    x=a
    a=b
    b=x
elif a>c:
    x=a
    a=c
    c=x
elif b>c:
    x=b
    b=c
    c=x
print(" Ba số theo thứ tự tăng dần là: ", a,b,c)
N= int(input("Nhập số nguyên: "))
N= str(N)
y=sorted(N)
print("Số sau khi sắp xếp theo thứ tự tăng dần là:", ''.join(y))