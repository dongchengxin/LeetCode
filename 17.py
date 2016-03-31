class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if not digits:
            return res
        self.dfs(digits,'',res)
        return res

    def dfs(self,digits,tmp,res):
        if not digits:
            res.append(tmp)
            return
        for c in self.d[digits[0]]:
            self.dfs(digits[1:],tmp+c,res)