#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:21:27 2020

@author: tyl
"""

class IOstring():
    def __init__(self):
        pass
        
    def getString(self):
        self.s = input("Input Something: ")
        
    def printString(self): 
        print(self.s.upper())
        
hello = IOstring()
hello.getString()
hello.printString()