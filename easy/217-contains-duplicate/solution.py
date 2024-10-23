class Solution(object):
    def containsDuplicate1(self, nums):        # solution 1
        nums_s = set(nums)
        return len(nums) != len(nums_s)
    
    def containsDuplicate2(self, nums):        # solution 2
        seen = dict()

        for n in nums:
            if n in seen:
                return True
            else:
                seen[n] = 0
            
        return False