"""
We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?

Here's an example: if the input was 49, we'd go through the following steps:

// start with 49
4 + 9 = 13

// move onto 13
1 + 3 = 4
We would then return 4.
"""

def sumDigits(num):

    if num <= 9:
        return num

    s = 0
    while s > 9 or num > 0:

        if num == 0:
            num = s
            s = 0

        s += num % 10
        num = num // 10

    return s


if __name__ == '__main__':
    print(sumDigits(1))
    print(sumDigits(49))
    print(sumDigits(439230))
