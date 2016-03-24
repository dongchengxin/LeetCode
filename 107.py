# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([root],res)
        return res

    def dfs(self, levelnodes, res):
        if not levelnodes or levelnodes[0] == None:
            return
        tmp = []
        res.insert(0,[])
        for node in levelnodes:
            res[0].append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        self.dfs(tmp,res)