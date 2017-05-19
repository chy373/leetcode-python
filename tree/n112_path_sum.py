'''
112. Path Sum Add to List
Difficulty: Easy Tags: Tree DFS

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # level order, BFS
    def hasPathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # empty tree
        if root is None:
            return False

        stack = [(root, total)]
        while stack:
            nextlevel = []
            for i in stack:
                node, remains = i
                gap = remains - node.val
                if gap == 0 and node.left is None and node.right is None:
                    return True
                else:
                    if node.left:
                        nextlevel.append((node.left, gap))
                    if node.right:
                        nextlevel.append((node.right, gap))
            stack = nextlevel
        return False

    # recursive
    def hasPathSum1(self, root, total):
        # empty tree
        if root is None:
            return False
        if total - root.val == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum1(root.left, total-root.val) or self.hasPathSum1(root.right, total-root.val)
