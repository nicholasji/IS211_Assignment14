#!user/bin/env python
#-*- coding: utf-8 -*-
#Week14


def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    while b:
        (a, b) = (b, (a % b))
    return a
  
def stringcomparison(s1, s2):
    if len(s1) < len(s2):
        return int(-1)
    elif len(s1) == len(s2):
        return int(0)
    elif len(s1) > len(s2):
        return int(1)



