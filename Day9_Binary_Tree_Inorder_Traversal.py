"""
Can you write a function to traverse a binary tree in-order, and print out the value of each node as it passes?

  4
   \
    5
   /
  6
The example would output [4, 6, 5] since there is no left child for 4, and 6 is visited in-order before 5.

The definition of a tree node is as follows:

function Node(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}
Follow up: you'll likely get the recursive solution first, could you do it iteratively?
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_recursive(node):

    if node:
        inorder_recursive(node.left)
        print(node.val, end=' ')
        inorder_recursive(node.right)

def inorder_iterative(node):

    s = list()
    current_node = node
    if node:
        while True:
            if current_node is not None:
                s.append(current_node)
                current_node = current_node.left
            elif s:
                current_node = s.pop()
                print(current_node.val, end=' ')
                current_node = current_node.right
            else:
                break


if __name__ == '__main__':
    n = Node(1)
    n.left = Node(2)
    n.left.left = Node(4)
    n.right = Node(3)

    inorder_recursive(n)
    inorder_iterative(n)
