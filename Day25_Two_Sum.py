"""
This is a classic and very common interview problem. Given an array of integers, return the indices of the two numbers in it that add up to a specific goal number.

So let's say our goal number was 10. Our numbers to sum to it would be 3 and 7, and their indices 1 and 3 respectively.

let arr = [1, 3, 6, 7, 9];
let goal = 10;
twoSum(arr, goal);
// [1, 3]
You may assume that each input would have exactly one solution. Additionally, you may not use the same element twice towards the sum. This means if given [1, 3] and a goal of 2, you cannot use 1 twice and return [0, 0].

Here's the function signature to fill in:

function twoSum(arr, goal) {
  return arr;
}
"""

def twoSum(arr, goal):

    d = dict()
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = i

    for i in range(len(arr)):
        n = goal - arr[i]
        if n in d.keys():
            return [i, d[n]]
    return []

if __name__ == '__main__':
    arr = [3, 2, 4, 1, 9]
    goal = 12
    print(twoSum(arr, goal))
