class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0:
            return result
        self.generate(n,n,'',result)
        return result

    def generate(self, m, n, tmp, result):
        if n == 0:
            result.append(tmp)
            return
        if m > 0:
            self.generate(m-1,n,tmp+'(',result)
        if n > m:
            self.generate(m,n-1,tmp+')',result)