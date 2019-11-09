"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

def findMissingInteger(inputArray):
    inputSet = set(inputArray)
    for i in range(1, len(inputSet) + 2):
        if not i in inputSet:
            return i

assert findMissingInteger([1,2,3,4]) == 5
assert findMissingInteger([2,3,4]) == 1
assert findMissingInteger([-2,-3,-4]) == 1
assert findMissingInteger([1, 3, 6, 4, 1, 2]) == 5
assert findMissingInteger([99999999]) == 1
assert findMissingInteger([9,9,9,9,9,9,9,9]) == 1
