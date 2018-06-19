#!/bin/python

def left_rotate(num, arr):
    # Since a "wrap around" will occur, we'll use modulus.
    # This will also allow the method to handle negative numbers.
    # Using this methodology will also prevent us from long-running 
    # calculations in actually rotating the list and creating multiple 
    # instances of arrays
    num = num % len(arr)
    return arr[num:] + arr[:num]
    

if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())
    
    print(" ".join(map(str, left_rotate(d, a))))
