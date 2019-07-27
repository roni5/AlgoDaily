"""
We're given a number n.
Write a function that returns the string representation of all numbers from 1 to n based on the following rules:
If it's a multiple of 3, represent it as "fizz".
If it's a multiple of 5, represent it as "buzz".
If it's a multiple of both 3 and 5, represent it as "fizzbuzz".
If it's neither, just return the number itself.
As such, fizzBuzz(15) would result in '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'.
"""

def fizzBuzz(n):

    if n <= 0:
        return ''

    res = ''

    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            res += 'fizzbuzz'
        elif i%3 == 0:
            res += 'fizz'
        elif i%5 == 0:
            res += 'buzz'
        else:
            res += str(i)
    return res

if __name__ == '__main__':
    print(fizzBuzz(0))
    print(fizzBuzz(1))
    print(fizzBuzz(15))
