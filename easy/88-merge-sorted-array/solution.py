class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p1, p2, p3 = m-1, m+n-1, n-1

        while p3 >= 0:
            if  p1 >= 0 and nums1[p1] > nums2[p3]:
                nums1[p2] = nums1[p1]
                p1 -= 1 
            else:
                nums1[p2] = nums2[p3]
                p3 -= 1
                
            p2 -= 1

            