"""
How would you write a function to detect a substring in a string?

If the substring can be found in the string, return the index at which it starts. Otherwise, return -1.

function detectSubstring(str, subStr) {
  return -1;
}
"""

def detectSubstring(str, subStr):
    n = len(str)
    m = len(subStr)

    for i in range(n-m+1):
        for j in range(m):
            if str[i+j] != subStr[j]:
                break
        if j+1 == m:
            return True
    return False

if __name__ == '__main__':
    print(detectSubstring('thepigflewwow', 'flew'))
    print(detectSubstring('twocanplay', 'two'))
    print(detectSubstring('wherearemyshorts', 'pork'))
