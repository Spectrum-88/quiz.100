#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 07:47:35 2020

@author: tyl
"""




#     Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#     Example:

# 0100,0011,1010,1001

#     Then the output should be:

# 1010

data = input("Enter binary numbers, separated by comma: ")
dataList = data.split(",")

for number in dataList:
    originalNumber = number
    length = len(number)
    sum = 0
    for digit in range(int(length)):
        sum = 2**digit * int(number[-1]) + sum
        number = number[0:-1]
        
    if sum % 5 == 0:
        print(originalNumber)

        
        
    