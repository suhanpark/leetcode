class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        a = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] <= max_l:
                    a += max_l - height[l]
                    l += 1
                else:
                    max_l = height[l]
                    l += 1
            else:
                if height[r] <= max_r:
                    a += max_r - height[r]
                    r -= 1
                else:
                    max_r = height[r]
                    r -= 1
        return a