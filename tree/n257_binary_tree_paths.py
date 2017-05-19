'''
257. Binary Tree Paths Add to List
Difficulty: Easy Tags: Tree DFS

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path+str(node.val))
            if node.right:
                stack.append((node.right, path+str(node.val)+'->'))
            if node.left:
                stack.append((node.left, path+str(node.val)+'->'))

    # dfs recursively; copy from discuss
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
