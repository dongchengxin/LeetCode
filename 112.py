# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.f = 0
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            self.f = 1
            return True
        if root.left:
            self.hasPathSum(root.left,sum - root.val)
        if root.right:
            self.hasPathSum(root.right,sum - root.val)
        return self.f == 1