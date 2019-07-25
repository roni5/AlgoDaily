"""
Here's the definition of an anagram: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

We are given two strings like "cinema" and "iceman" as inputs. Can you write a method isAnagram(str1, str2) that will return true or false depending on whether the strings are anagrams of each other?
"""

def isAnagram(str1, str2):
    str1CharacterCount = dict()
    for ch in str1:
        if ch in str1CharacterCount:
            str1CharacterCount[ch] += 1
        else:
            str1CharacterCount[ch] = 1

    for ch in str2:
        if ch in str1CharacterCount:
            str1CharacterCount[ch] -= 1
        else:
            return False

    for ch, value in str1CharacterCount.items():
        if value != 0:
            return False
    return True


if __name__ == '__main__':
    print(isAnagram('cinema', 'iceman'))
