"""
You're given a number n. Can you write a method sumOfAllPrimes that finds all prime numbers smaller than or equal to n, and returns a sum of them?

For example, we're given the number 15. All prime numbers smaller than 15 are:

2, 3, 5, 7, 11, 13

They sum up to 41, so sumOfAllPrimes(15) would return 41.
"""

def isPrime(n):

    if n == 1:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    else:
        prime_num = 5
        while prime_num <= 7:
            if n % prime_num == 0:
                return False
            prime_num += 2

    return True

def sumOfAllPrimes(num):

    if num <= 1:
        return False

    s = 0
    for i in range(2, num+1):
        if isPrime(i):
            s += i
    return s

if __name__ == '__main__':
    print(sumOfAllPrimes(55))
