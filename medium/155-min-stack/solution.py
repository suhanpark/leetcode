class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.mins[-1]) if self.mins else val
        self.mins.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
