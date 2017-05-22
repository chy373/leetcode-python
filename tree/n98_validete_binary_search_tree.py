'''
98. Validate Binary Search Tree Add to List
Difficulty: Medium Tags: Tree DFS
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # in-order traversal, it's an ascending array, compare current node with previous node
    def isValidBST(self, root):
        self.prev = None
        return self.validate(root, self.prev)

    def validate(self, node, prev):
        if not node:
            return True
        if not self.validate(node.left, self.prev):
            return False
        if not self.prev and self.prev.val >= node.val:
            return False
        self.prev = node
        return self.validate(node.right, self.prev)

    def isValidBST1(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
