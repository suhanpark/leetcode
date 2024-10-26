class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        max_l = 0

        for i, n in enumerate(numset):
            if n-1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1

                max_l = max(length, max_l)
            
        return max_l