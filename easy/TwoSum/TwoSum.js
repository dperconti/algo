/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/

function twoSum(arr, S) {
  var sums = [];
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


console.assert(twoSum([10, 15, 3, 7], 17) == Array([7, 10]));
console.assert(twoSum([10, 15, 3, 7, 8, 9, 10], 19) == [(9, 10), (10, 9)]);
console.assert(twoSum([2, 7, 11, 15], 9) == [(7, 2)]);
console.assert(twoSum([6, 7, 11, 15, 3, 6, 5, 3], 6) == [(3, 3)]);
console.assert(twoSum([3, 5, 2, -4, 8, 11], 7) == [];