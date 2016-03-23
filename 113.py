# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        s = []
        self.dlr(root,[],s,sum)
        return s
        
    def dlr(self,root,path,s,num):
        if not root:
            return
        if not root.left and not root.right:
            if sum(path+[root.val]) == num:
                s.append(path+[root.val])
                return
        self.dlr(root.left,path+[root.val],s,num)
        self.dlr(root.right,path+[root.val],s,num)