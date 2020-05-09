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

# Use .count() and .remove to rewrite the program again. 
for i in dataList:
    if dataList.count(i) > 1:
        dataList.remove(i)

dataList.sort()

print(" ".join(dataList))

