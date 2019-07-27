"""
In a given array of numbers, one element will show up once and the rest will show up twice. Can you find that number in O(n) linear time?

lonelyNumber([4, 4, 6, 1, 3, 1, 3])
// 6

lonelyNumber([3, 3, 9])
// 9
"""

def lonelyNumber(arr):
    numOccurence = list()

    for i in range(len(arr)):
        if arr[i] in numOccurence:
            numOccurence.remove(arr[i])
        else:
            numOccurence.append(arr[i])

    return numOccurence[0]


if __name__ == '__main__':
    print(lonelyNumber([4, 4, 6, 1, 3, 1, 3]))
    print(lonelyNumber([3, 3, 9]))
    print(lonelyNumber([1]))
