class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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