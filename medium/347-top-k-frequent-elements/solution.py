class Solution(object):
    def topKFrequent1(self, nums, k): # solution 1
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen = {}

        for n in nums: # O(n)
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        
        
        k_ranked = sorted(seen.items(), key = lambda x: x[1], reverse=True)[:k] # O(nlogn)
        return [tup[0] for tup in k_ranked] # O(1)
    
    def topKFrequent2(self, nums, k): # solution 2
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen = {}

        for n in nums: # O(n)
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)] # O(n)

        for n, f in seen.items(): # O(n)
            buckets[f].append(n)

        result = []
        i = -1
        while len(result) != k: # O(n)
            for n in buckets[i]:
                result.append(n)
            i -= 1

        return result