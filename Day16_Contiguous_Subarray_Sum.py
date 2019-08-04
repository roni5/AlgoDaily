"""
Given an array of numbers, return true if there is a contiguous subarray that sums up to a certain number n.

const arr = [1, 2, 3], sum = 5
subarraySum(arr, sum)
// true

const arr = [11, 21, 4], sum = 9
subarraySum(arr, sum)
// false
In the above examples, 2, 3 sum up to 5 so we return true. On the other hand, no subarray in [11, 21, 4] can sum up to 9.
"""

def subarraySum(arr, sum):

    if arr[0] == sum:
        return True

    curr_sum, arr_counter = arr[0], 0
    for i in range(1, len(arr)):
        curr_sum += arr[i]
        if curr_sum == sum:
            return True
        elif curr_sum > sum:
            while curr_sum > sum:
                curr_sum -= arr[arr_counter]
                arr_counter += 1
            if curr_sum == sum:
                return True
    return False

if __name__ == '__main__':
    arr, sum = [11, 21, 4], 9
    print(subarraySum(arr, sum))
