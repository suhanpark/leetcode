from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        nums_s = set(nums)
        return len(nums) != len(nums_s)
    
    def hasDuplicate2(self, nums: List[int]) -> bool:
        # solution 2
        seen = dict()

        for n in nums:
            if n in seen:
                return True
            else:
                seen[n] = 0
            
        return False