#!/bin/python

import math
import os
import random
import re
import sys

words = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
         

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m == 0:
        return words[h - 1] + " o' clock"
    
    if m < 31:
        connector = " minutes past "
        if m == 1 or m == 59:
            connector = " minute past "
        if m == 15 or m == 30:
            connector = " past "
        return words[m - 1] + connector + words[h - 1] 
    else:
        connector = " minutes to "
        if m == 1 or m == 59:
            connector = " minute to "
        if m == 45:
            connector = " to "
        return words[60 - m - 1] + connector + words[h] 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(raw_input())

    m = int(raw_input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()