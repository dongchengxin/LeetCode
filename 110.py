# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Unbalanced(BaseException):
    pass

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        try:
            self.depth(root)
        except Unbalanced:
            return False
        return True

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left - right) > 1:
            raise Unbalanced()
        return max(left,right) + 1