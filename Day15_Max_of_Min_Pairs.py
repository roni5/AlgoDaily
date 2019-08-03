"""
We have an array of length 2 * n (even length) that consists of random integers.
[1, 3, 2, 6, 5, 4]
We are asked to create pairs out of these integers, like such:
[[1, 3], [2, 6], [5, 4]]
How can we divide up the pairs such that the sum of smaller integers in each pair is maximized?
Here's an example input: [3, 4, 2, 5]. The return value is 6 because the maximum sum of pairs is 6 = min(2, 3) + min(4, 5).
Note that negative numbers may also be included.
"""

def maxOfMinPairs(arr):
    arr.sort()

    s = 0
    for i in range(0, len(arr), 2):
        s += min(arr[i], arr[i+1])
    return s

if __name__ == '__main__':
    print(maxOfMinPairs([1, 3, 2, 6, 5, 4]))
    print(maxOfMinPairs([ 3, 4, 2, 5 ]))
