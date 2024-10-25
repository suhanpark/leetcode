class Solution(object):
    def productExceptSelf1(self, nums): # solution 1
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        front, back = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))] # O(n)

        for i in range(len(nums)): # O(n)
            if i == 0:
                front[i], back[-i-1] = nums[i], nums[-i-1]
            else:
                front[i], back[-i-1] = nums[i]*front[i-1], nums[-i-1]*back[-i]

        result = []
        for i in range(len(nums)): # O(n)
            if i == 0:
                result.append(back[i+1])
            elif i == len(nums)-1:
                result.append(front[i-1])
            else:
                result.append(front[i-1]*back[i+1])

        return result
    
    def productExceptSelf2(self, nums): # solution 2
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [1] * len(nums) # O(n)

        front = 1
        for i in range(len(nums)): # O(n)
            res[i] = front
            front *= nums[i]
        
        back = 1
        for i in range(len(nums)): # O(n)
            res[-i-1] *= back
            back *= nums[-i-1]
        
        return res