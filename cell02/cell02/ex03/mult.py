#!/usr/bin/env python3
a = int(input())
b = int(input())
c = a*b
if c > 0:
    print(a,"a",b,"=",c,"The result is positive")

elif c < 0:
    print(a,"a",b,"=",c,"the result is negative")
else:
    print(a,"a",b,"=",c,"the result is both positive and nagative")