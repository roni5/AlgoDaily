"""
We're given an array of integers like the following:

[0, 1, 2, 3, 4, 5, 6, 7, 8]
We then rotate it at a random pivot so that the section after the pivot comes before. So say we put our pivot between 5 and 6:

[6, 7, 8, 0, 1, 2, 3, 4, 5]
Can you find the smallest element in O(log n) time? Assume that there are no repeat numbers.

Here are some other examples: given [4, 5, 1, 2, 3], we'd get 1.

In the event that there's a missing number in the sequence like [5, 6, 7, 0, 1, 2, 3] (where 4 isn't present), the output would still be 0.
"""

def getMinimum(arr, low, high):
    # this condition needed to handle the case when array is not rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[high]

    mid = round((low + high) / 2)

    # check if mid+1 is minimum element. Consider the cases like [3, 4, 5, 1, 2]
    if arr[mid] > arr[mid+1] and mid < high:
        return arr[mid+1]

    # check if mid itself is minimum element
    if arr[mid] < arr[mid-1] and mid > low:
        return arr[mid]

    # Decide whether we need to go left half or right half
    if arr[high] > arr[mid]:
        return getMinimum(arr, low, mid-1)
    return getMinimum(arr, mid+1, high)

if __name__ == '__main__':
    arr = [6, 7, 8, 9, 10, 3, 4, 5]
    print(getMinimum(arr, 0, len(arr)-1))