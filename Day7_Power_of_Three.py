"""
Given an integer num, write a method to determine if it is a power of 3.

console.log(powerOfThree(9));
// true

"""

def powerOfThree(n):
    if n < 1:
        return False

    while n/3 >= 1:
        n = n/3

    return n == 1

if __name__ == '__main__':
    print(powerOfThree(9))
    print(powerOfThree(729))
    print(powerOfThree(7))
