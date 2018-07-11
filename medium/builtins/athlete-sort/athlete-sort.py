#!/bin/python

import math
import os
import random
import re
import sys

def pretty_print(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print a[i][j],
        print ""

if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    k = int(raw_input())
    
    # take second element for sort
    def sortByElement(elem):
        return elem[k]

    # sort list with key
    sortedList = sorted(arr, key=sortByElement)
    
    pretty_print(sortedList)
    
    

