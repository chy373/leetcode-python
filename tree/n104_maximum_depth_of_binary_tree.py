'''
104. Maximum Depth of Binary Tree
Difficulty: Easy Tags: Tree, DFS

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # recursive
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative BFS level order traversal
    def maxDepth1(self, root):
        pass

if __name__ == "__main__":
    t = TreeNode(0)
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t.left = t1
    t1.left =t2
    s = Solution()
    print s.maxDepth(t)
    print s.maxDepth1(t)
