"""
You're given a string of random alphanumerical characters with a length between 0 and 1000.

Write a method to return the first character in the string that does not repeat itself later on.

firstNonRepeat('asdfsdafdasfjdfsafnnunl') should return 'j'
"""

import re

def firstNonRepeat(str):
    if len(str) <= 1:
        return str

    str = re.sub(r'\s+', '', str)

    count = dict()
    for ch in str:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for key in count:
        if count[key] == 1:
            return key

if __name__ == '__main__':
    print(firstNonRepeat(''))
    print(firstNonRepeat('a'))
    print(firstNonRepeat('oh my god dude where is my car'))
    print(firstNonRepeat('asdfsdafdasfjdfsafnnunlfdffvxcvsfansd'))