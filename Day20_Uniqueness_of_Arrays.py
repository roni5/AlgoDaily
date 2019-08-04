"""
Given an array, return just the unique elements without using any built-in Array filtering. In other words, you're removing any duplicates.

Note: Order needs to be preserved, so no sorting should be done.

function uniques(arr) {
  // fill in
}

let arr = [3, 5, 6, 9, 9, 4, 3, 12]
uniques(arr);
// [3, 5, 6, 9, 4, 12]

arr = [13, 5, 3, 5, 8, 13, 14, 5, 9]
uniques(arr);
// [13, 5, 3, 8, 14, 9]
"""

def uniques(arr):
    filterArr = list()

    for i in range(len(arr)):
        if arr[i] not in filterArr:
            filterArr.append(arr[i])
    return filterArr

if __name__ == '__main__':
    print(uniques([13, 5, 3, 5, 8, 13, 14, 5, 9]))
