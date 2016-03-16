class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.s.pop(len(self.s) - 1)

    def top(self):
        """
        :rtype: int
        """
        return self.s[len(self.s) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s) == 0