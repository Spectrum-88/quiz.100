#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 07:47:35 2020

@author: tyl
"""



#     Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

#     Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

#     Then, the output should be:

# again and hello makes perfect practice world

data = input("Enter strings, separated with spaces: ")
dataList = data.split(" ")
dataList.sort()

n = len(dataList)
newList = []

for i in range(n-1):
    # Only execute to the [-2] or n-1 item, because it compares [-2] and [-1]
    # If you execute to the [-1] or last item, "IndexError: list index out of range"
    # It would compare [-1] and Nothing...
    
    if dataList[i] != dataList[i+1]:
        newList.append(dataList[i])

newList.append(dataList[-1])
# Always print the last item. Because the previous identical items would not be printed. 

print(" ".join(newList))
# practice weird .join() again. 