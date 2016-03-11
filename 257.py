# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.dfs(root,"",result)
        return result

    def dfs(self,node,path,res):
        """
        :type node: TreeNode
        :rtype: Lise[str]
        """
        if not node.left and not node.right:
            res.append(path + str(node.val))
        if node.left:
            self.dfs(node.left,path + str(node.val) + "->",res)
        if node.right:
            self.dfs(node.right,path + str(node.val) + "->",res)