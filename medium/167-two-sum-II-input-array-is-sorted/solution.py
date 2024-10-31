class Solution(object):
    def twoSum1(self, numbers, target): # solution 1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums = {n: i for i, n in enumerate(numbers)}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in nums and nums[diff] != i:
                return [min(nums[diff], i)+1, max(nums[diff], i)+1]
        
        return []

    def twoSum2(self, numbers, target): # solution 2
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l, r = 0, len(numbers)-1
        
        while numbers[l]+numbers[r] != target:
            if numbers[l]+numbers[r] > target:
                r -= 1
            elif numbers[l]+numbers[r] < target:
                l += 1
          
        return [l+1, r+1]