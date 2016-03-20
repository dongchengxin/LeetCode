class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.ls = 0
        self.mindex = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.minstack.append(x)
        self.ls += 1
        if x < self.minstack[self.mindex]:
            self.mindex = self.ls - 1

    def pop(self):
        """
        :rtype: nothing
        """
        if self.ls > 0:
            self.ls -= 1
            self.minstack.pop(self.ls)
        if self.mindex == self.ls:
            self.mindex = 0
            for i in range(1,self.ls):
                if self.minstack[i] < self.minstack[self.mindex]:
                    self.mindex = i

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[self.ls - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.ls > 0:
            return self.minstack[self.mindex]