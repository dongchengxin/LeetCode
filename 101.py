# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Dissymmetric(BaseException):
    pass

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        try:
            self.bfs([root])
        except Dissymmetric:
            return False
        return True

    def bfs(self,levelnodes):
        if not levelnodes or levelnodes[0] == None:
            return
        tmp = []
        l = len(levelnodes)
        if l != 1 and l % 2 != 0:
            raise Dissymmetric()
        for i in range((l+1)/2):
            if levelnodes[i].left and not levelnodes[-i-1].right or not levelnodes[i].left and levelnodes[-i-1].right:
                raise Dissymmetric()
            if levelnodes[i].right and not levelnodes[-i-1].left or not levelnodes[i].right and levelnodes[-i-1].left:
                raise Dissymmetric()
            if levelnodes[i].val != levelnodes[-i-1].val:
                raise Dissymmetric()
        for i in range(l):
            if levelnodes[i].left:
                tmp.append(levelnodes[i].left)
            if levelnodes[i].right:
                tmp.append(levelnodes[i].right)
        self.bfs(tmp)