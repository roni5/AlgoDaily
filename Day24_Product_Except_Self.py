"""
If we are given an array of integers, can you return an output array such that each corresponding input's elements returns the product of the input array except itself?

This can be hard to explain, so let's take an array: [1, 2, 4, 16]

What we want to return is [128, 64, 32, 8]. This is because 2 x 4 x 16 = 128, 1 x 4 x 16 = 64, 1 x 2 x 16 = 32, and 1 x 2 x 4 = 8.

In other words, output[i] is equal to the product of all the elements in the array other than input[i].

Can you solve this in O(n) time without division?
"""

def productArray(arr):

    n = len(arr)

    # Allocate memory for temporary arrays left[] and right[]
    left = [0]*n
    right = [0]*n

    # Allocate memory for product array
    prod = [0]*n

    # left most array is always 1
    left[0] = 1

    # rightmost most element of right array is always 1
    right[n-1] = 1

    # construct the left array
    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]

    # construct the right array
    for j in range(n-2, -1, -1):
        right[j] = arr[j+1] * right[j+1]

    # construct product array
    for i in range(n):
        prod[i] = left[i] * right[i]

    # print the product array
    for i in range(n):
        print(prod[i], end=' ')

if __name__ == '__main__':
    productArray([10, 3, 5, 6, 2])
