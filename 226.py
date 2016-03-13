# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invertNode(root)
        return root
        
    def invertNode(self, node):
        if not node:
            return
        if node.left or node.right:
            tmp = node.left
            node.left = node.right
            node.right = tmp
        self.invertNode(node.left)
        self.invertNode(node.right)