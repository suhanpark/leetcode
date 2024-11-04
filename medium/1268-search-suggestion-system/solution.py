class MedianFinder(object):

    def __init__(self):
        self.small, self.big = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num)

        if self.small and self.big and -self.small[0] > self.big[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
            
        if len(self.small) > len(self.big) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)

        if len(self.small) + 1 < len(self.big):
            val = -heapq.heappop(self.big)
            heapq.heappush(self.small, val)

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.small)+len(self.big)) % 2 == 0:
            return float((-self.small[0] + self.big[0])) / 2
        else:
            if len(self.small) > len(self.big):
                return -self.small[0]
            else:
                return self.big[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()