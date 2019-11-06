"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def twoSum(nums, target):
    sums = []
    hashTable = set()
    for num in nums:
        diff = target - num
        if diff in hashTable:
            sums.append((num, diff))
        hashTable.add(num)
    return sums


assert twoSum([10, 15, 3, 7], 17) == [(7, 10)]
assert twoSum([10, 15, 3, 7, 8, 9, 10], 19) == [(9, 10), (10, 9)]
assert twoSum([2, 7, 11, 15], 9) == [(7, 2)]
assert twoSum([6, 7, 11, 15, 3, 6, 5, 3], 6) == [(3, 3)]
