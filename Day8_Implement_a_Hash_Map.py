"""
Can you implement the JS Map class from scratch? Only two methods are necessary-- get and set. Do not use JS Objects ({} notation) for this exercise.

Note: Regular Javascript objects and the Map class are both simple key-value hash tables/associative arrays, with a few key differences:

A Map object can iterate through its elements in insertion order, whereas JavaScript's Objects don't guarantee order. In addition, Objects have default keys due to their prototype, and Maps don't come with default keys. Here's a good breakdown of the two. For the purpose of this exercise, let's assume the same functionality for both.

For the two methods you'll define:

get(key: string) should be given a key, and return the value for that key.
set(key: string, val: string) should take a key and a value as parameters, and store the pair.
Additionally, we've supplied the below hashing function hashStr. It tries to avoid collision, but is not perfect. It takes in a string value and returns an integer.

function hashStr(str) {
    let finalHash = 0;
    for (let i = 0; i < str.length; i++) {
        const charCode = str.charCodeAt(i);
        finalHash += charCode;
    }
    return finalHash;
}

console.log(hashStr('testKey'))
Let's call our new class the Hashmap class:

const m = new Hashmap();
m.set('name', 'Jake');
console.log(m.get('name'));
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hashmap:

    def __init__(self):
        self.storage = [None for _ in range(16)]
        self.size = 0

    def hashStr(self, key):
        if isinstance(key, int):
            return key

        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result

    def position(self, key_hash):
        return key_hash % 16

    def set(self, key, val):
        p = Node(key, val)
        key_hash = self.hashStr(key)
        index = self.position(key_hash)

        if not self.storage[index]:
            self.storage[index] = [p]
            self.size += 1
        else:
            list_at_index = self.storage[index]
            if p not in list_at_index:
                self.storage[index] = [p]
                self.size += 1
            else:
                for i in self.storage[index]:
                    if i == p:
                        i.value = val
                        break

    def get(self, key):
        key_hash = self.hashStr(key)
        index = self.position(key_hash)

        if not self.storage[index]:
            return None
        else:
            list_at_index = self.storage[index]
            for i in self.storage[index]:
                if i.key == key:
                    return i.value
        return None



if __name__ == '__main__':
    m = Hashmap()
    m.set('name', 'Jake')
    print(m.get('name'))
    m.set('name', 'Jane')
    print(m.get('name'))
