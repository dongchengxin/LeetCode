class Queue(object):
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
        self.s.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.s[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.s) == 0:
            return True
        else:
            return False