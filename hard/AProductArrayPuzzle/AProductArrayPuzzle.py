"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def productArray(arr, n):
    left, right, prod = [1] * len(arr), [1] * len(arr), [1] * len(arr)

    # Build the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    # Build the right array
    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Build the product array using left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]

    return prod

assert productArray([10, 3, 5, 6, 2], 5) == [180, 600, 360, 300, 900]
assert productArray([1, 2, 3, 4, 5], 5) == [120, 60, 40, 30, 24]
assert productArray([1, 2], 2) == [2, 1]
assert productArray([800, 1, 5, 23, 7, 5, 7, 8, 9, 6, 4, 7, 8, 998, 6, 54, 32], 17) ==[28211177904537600, 22568942323630080000, 4513788464726016000, 981258361896960000, 3224134617661440000, 4513788464726016000, 3224134617661440000, 2821117790453760000, 2507660258181120000, 3761490387271680000, 5642235580907520000, 3224134617661440000, 2821117790453760000, 22614170664960000, 3761490387271680000, 417943376363520000, 705279447613440000]
