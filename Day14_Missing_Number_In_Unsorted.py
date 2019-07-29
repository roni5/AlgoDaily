"""
Assume we're given an unsorted array of numbers such as this:

[ 2, 5, 1, 4, 9, 6, 3, 7 ]

We are told that there are a series of n consecutive numbers, with a lower bound and upper bound.

There is one consecutive number missing. In this case, if the lower bound is 1 and the upper bound is 9, it's 8.

const arr = [ 2, 5, 1, 4, 9, 6, 3, 7 ];
const lowerBound = 1;
const upperBound = 9;

missingInUnsorted(arr, lowerBound, upperBound);
// 8
Can you find the missing number in O(n) time? Can you do it without sorting?
"""

def missingInUnsorted(arr, lowerBound, upperBound):
    actualSum = sum([n for n in arr])
    upperLimitSum = upperBound * (upperBound + 1) / 2

    lowerLimitSum = lowerBound * (lowerBound - 1) / 2

    theoreticalSum = upperLimitSum - lowerLimitSum

    return theoreticalSum - actualSum

if __name__ == '__main__':
    print(missingInUnsorted([ 2, 5, 1, 4, 9, 6, 3, 8], 1, 9))
