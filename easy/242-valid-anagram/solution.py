class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sd, td = dict(), dict()

        for i in range(len(s)):
            if s[i] in sd:
                sd[s[i]] += 1
            else:
                sd[s[i]] = 1
            
            if t[i] in td:
                td[t[i]] += 1
            else:
                td[t[i]] = 1
            
        return sd == td 