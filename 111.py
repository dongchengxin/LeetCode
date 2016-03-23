# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = 0
        if root:
            self.bfs(root,1)
        return self.d

    def bfs(self,root,d):
        if not root:
            return
        if not root.left and not root.right:
            if self.d == 0 or self.d > d:
                self.d = d
            return
        self.bfs(root.left,d+1)
        self.bfs(root.right,d+1)