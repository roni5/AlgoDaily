"""
Given a string str, can you write a method that will return True if is a palindrome and False if it is not? If you'll recall, a palindrome is defined as "a word, phrase, or sequence that reads the same backward as forward". For now, assume that we will not have input strings that contain special characters or spaces, so the following examples hold:

let str = 'thisisnotapalindrome';
isPalindrome(str);
// false

str = 'racecar';
isPalindrome(str);
// true
For an extra challenge, try to ignore non-alphanumerical characters. The final solution that we present will handle all edge cases.
"""

import re

def isPalindrome(str):

    strList = list(re.sub(r'\s+', '', str))
    length = round(len(strList)/2)

    for i in range(length):
        if strList[i].lower() != strList[len(strList)-i-1].lower():
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome('A Santa Lived As a Devil At NASA'))
    print(isPalindrome('racecar'))
    print(isPalindrome('a'))
    print(isPalindrome('gold'))
