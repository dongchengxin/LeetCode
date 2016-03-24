# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Different(BaseException):
    pass

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        try:
            self.same(p,q)
        except Different:
            return False
        return True

    def same(self,p,q):
        if not q and not p:
            return
        if p and not q or q and not p:
            raise Different()
        if p.val != q.val:
            raise Different()
        if p.left and not q.left or p.right and not q.right or not p.left and q.left or not p.right and q.right:
            raise Different()
        if p.left:
            self.same(p.left,q.left)
        if p.right:
            self.same(p.right,q.right)