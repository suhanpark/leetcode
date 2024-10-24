class Solution(object):
    def groupAnagrams1(self, strs): # solution 1
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = dict()

        for word in strs:
            w = ''.join(sorted(word))

            if w in seen:
                seen[w].append(word)
            else:
                seen[w] = [word]            
        
        return list(seen.values())
    
    def groupAnagrams2(self, strs): # solution 2
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}

        for word in strs:
            key = [0]*26

            for c in word:
                key[ord(c) - ord('a')] += 1

            key = tuple(key)

            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]

        return list(seen.values())
