/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/
function findMissingInteger(inputArray) {
  for (i = 1; i < inputArray.length + 2; i++) {
    if(!inputArray.includes(i)) return i;
  }
}


console.log(findMissingInteger([1,2,3,4]) === 5)
console.log(findMissingInteger([2,3,4]) === 1)
console.log(findMissingInteger([-2,-3,-4]) === 1)
console.log(findMissingInteger([1, 3, 6, 4, 1, 2]) === 5)
console.log(findMissingInteger([99999999]) === 1)
console.log(findMissingInteger([9,9,9,9,9,9,9,9]) === 1)
