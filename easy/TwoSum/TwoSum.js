/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/

function twoSum(arr, S) {
  const sums = new Array();
  var hashTable = {};
  for (var i = 0; i < arr.length; i++) {
    var sumMinusElement = S - arr[i];
    if (hashTable[sumMinusElement.toString()] !== undefined) {
      sums.push([arr[i], sumMinusElement]);
    }
    hashTable[arr[i].toString()] = arr[i];
  }
  return sums;
}

[[7, 10]].equals(twoSum([10, 15, 3, 7], 17));
[[9, 10], [10, 9]].equals(twoSum([10, 15, 3, 7, 8, 9, 10], 19));
[[7, 2]].equals(twoSum([2, 7, 11, 15], 9));
[[3, 3]].equals(twoSum([6, 7, 11, 15, 3, 6, 5, 3], 6));
[[2, 5], [11, -4]].equals(twoSum([3, 5, 2, -4, 8, 11], 7));
