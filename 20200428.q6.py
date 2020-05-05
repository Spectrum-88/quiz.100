#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:27:45 2020

@author: tyl
"""



C = 50
D = input("Input D value: ")
H = 30
answerList = []

def calculator(D):
    Q = (2 * C * D / H)**0.5
    return int(Q)

# from math import *
# 導入math才能使用sqrt，不然使用 **0.5 也有平方根的效果，不是^

listD = D.split(',')
# listD不必先宣告，因為.split會自動產生一個list

for i in listD:
    answer = calculator(int(i))
    answerList.append(str(answer))
    
print(",".join(answerList))
# 利用.join 將list 的元素連接起來並印出，以符合題目的條件
# .join一定使用string，要先轉換int --> string