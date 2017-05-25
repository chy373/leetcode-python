'''
102. Binary Tree Level Order Traversal Add to List
Difficulty: Medium Tags: Tree BFS

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack, res = [root], []
        while stack:
            res.append([i.val for i in stack])
            nextlevel = []
            for node in stack:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            stack = nextlevel
        return res

    def levelOrder1(self, root):
        res, level = [], [root]
        while root and level:
            res.append([i.val for i in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res
