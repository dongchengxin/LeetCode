class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        l = -1
        for c in s:
            if c in '({[':
                stack.append(c)
                l += 1
            elif c == ')':
                if l >= 0 and stack[l] == '(':
                    stack.pop()
                    l -= 1
                else:
                    return False
            elif c == '}':
                if l >= 0 and stack[l] == '{':
                    stack.pop()
                    l -= 1
                else:
                    return False
            elif c == ']':
                if l >= 0 and stack[l] == '[':
                    stack.pop()
                    l -= 1
                else:
                    return False
        return stack == []