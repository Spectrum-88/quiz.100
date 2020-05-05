#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:23:51 2020

@author: tyl
"""


x = int(input("Enter an integer: "))
ans = {}

for i in range(1, x + 1):
    ans[i] = i * i

print(ans)

