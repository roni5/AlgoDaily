"""
We have an unsorted array of integers such as the following:

[-2, -1, 0, 1, 3]
In the above example, the minimum number is -2 and the maximum is 3.

This means there is an expected range (defined as the collection of values between the minimum and maximum values) of [-2, -1, 0, 1, 2, 3] for the array.

But look at the example again:

[-2, -1, 0, 1, 3]
We're missing a number: 2. The smallest missing positive integer for our input array is 2.

Can you write a method that takes such an array and returns the first missing positive integer?

leastMissingPositive([1, 2, 3, 0])
// 4
In the above example, it is 4 since we already have 0 through 3. Have your code run in O(n) time with constant space.
"""

def seperation(arr):
    # seperate the positive and negative number in array
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return j

def findMissingPositive(arr, size):
    for i in range(size):
        x = abs(arr[i])
        if x - 1 < size and arr[x-1] > 0:
            arr[x-1] = -arr[x-1]

    for i in range(size):
        if arr[i] > 0:
            return i+1

    return size+1

def leastMissingPositive(arr):
    shift = seperation(arr)
    arr2 = [None] * (len(arr)-shift)
    j = 0
    for i in range(shift, len(arr)):
        arr2[j] = arr[i]
        j += 1

    return findMissingPositive(arr2, j)

if __name__ == '__main__':
    print(leastMissingPositive([3, 5, -1, 1]))
