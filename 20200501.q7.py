# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#     Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

#     Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

#     Then, the output of the program should be:

#     [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#       3, 5 means big 3 groups, each group with 5 items. 

inputData = input("Input 2 integers, seperate with comma. ex: 3, 2: ")
inputDataList = inputData.split(",")

x = int(inputDataList[0])
y = int(inputDataList[1])

answerList = []
subList = []

# I was thinking about this: 
# for i in range(x):
#    for j in range(y):
#
#        answerList[i][j] = i * j 
# IndexError: list assignment index out of range
# The above syntax only can change the value of list
# Rather than create or assign a new value in list. 

for i in range(x):
    subList = []
    for j in range(y):
        subList.append(i*j)
    answerList.append(subList)

# 技巧: 先把最底層的List弄完，再加回到上一層 list

print(answerList)
        
        