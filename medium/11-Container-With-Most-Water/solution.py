class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_a = 0
        
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_a = max(h*w, max_a)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_a
                