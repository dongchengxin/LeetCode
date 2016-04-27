class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i, c in enumerate(s):
            if not stack:
                stack.append(i)
            else:
                if s[i] == ')' and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        end = len(s)
        if not stack:
            return end
        result = 0
        while stack:
            start = stack.pop()
            result = max(result, end - start - 1)
            end = start
        result = max(result, end)
        return result
