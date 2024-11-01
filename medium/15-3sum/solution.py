class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            j, k = i+1, len(nums)-1
            
            while j < k:
                s = n + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    last = [n, nums[j], nums[k]]
                    result.append(last)

                    j += 1
                    k -= 1
                    while nums[j] == nums[j -1] and j < k:
                        j += 1
            
        return result