#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:33:00 2020

@author: tyl
"""




#     Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#     Suppose the following input is supplied to the program:

# without,hello,bag,world

#     Then, the output should be:

# bag,hello,without,world

data = input("Input words, separated by comma: ")
dataList = data.split(",")
dataList.sort()

# https://www.itread01.com/content/1502116686.html
# .join 的用法真的與眾不同，不背是沒辦法的

dataString = ','.join(dataList)
print(dataString)