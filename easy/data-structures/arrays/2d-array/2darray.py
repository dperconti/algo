#!/bin/python

import os

# Complete the hourglassSum function below.
def hoursum(arr, r, c):
    return sum(arr[r - 1][c-1:c+2]) + arr[r][c] + sum(arr[r + 1][c-1:c+2])

def hourglassSum(arr):
    ans = max(hoursum(arr, r, c) for r in range(1,5) for c in range(1,5))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

