"""
You are given a string that contains alphabetical characters (a - z, A - Z) and some other characters ($, !, etc.). For example, one input may be:

'sea!$hells3'

Can you reverse only the alphabetical ones?

reverseOnlyAlphabetical('sea!$hells3');
// 'sll!$ehaes3'
"""

import re

def reverseOnlyAlphabetical(str):
    strList = list(re.sub(r'\s+', '', str))

    startPointer = 0
    endPointer = len(strList)-1

    while startPointer <= endPointer:
        if strList[startPointer].isalpha():
            if strList[endPointer].isalpha():
                strList[startPointer], strList[endPointer] = strList[endPointer], strList[startPointer]
                startPointer += 1
                endPointer -= 1
            else:
                endPointer -= 1
        else:
            startPointer += 1

    return ''.join(strList)

if __name__ == '__main__':
    print(reverseOnlyAlphabetical('sea!$hells3'))
    print(reverseOnlyAlphabetical('1kas90jda3'))
