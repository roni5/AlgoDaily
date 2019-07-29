"""
You're given an array of strings containing alphabetical characters and certain $ characters. A $ represents a DELETE action whereby the character before it is deleted.

Each of these strings will be run through a method to operate on the $ DELETE action. We want to find out if the final string is the same for all of them. Let's take an example:

const input = ["f$st", "st"]
isDollarDeleteEqual(input);
// true
// true because both become "st"
Given the below function signature, can you find a solution in O(n) time and constant space?

function isDollarDeleteEqual(arr) {
  return;
}

"""

def isDollarDeleteEqual(arr):
    str1 = list()
    str2 = list()

    for ch in arr[0]:
        if ch == '$' and len(str1) > 0:
            str1.pop()
        elif ch != '$':
            str1.append(ch)

    for ch in arr[1]:
        if ch == '$' and len(str2) > 0:
            str2.pop()
        elif ch != '$':
            str2.append(ch)

    return ''.join(str1) == ''.join(str2)

if __name__ == '__main__':
    print(isDollarDeleteEqual(['f$ec', 'ec']))
    print(isDollarDeleteEqual(['ab$$', 'c$d$']))
    print(isDollarDeleteEqual(['b$$p', '$b$p']))
