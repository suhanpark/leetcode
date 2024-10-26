import re

class Solution(object):
    def isPalindrome1(self, s): # solution 1
        """
        :type s: str
        :rtype: bool
        """
        
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        for i in range(len(s)):
            if s[i].lower() != s[-i-1].lower():
                return False
        
        return True

    def isPalindrome2(self, s): # solution 2
        """
        :type s: str
        :rtype: bool
        """
        
        i, j = 0, len(s)-1

        while i <= j:
            if s[i].isalnum():
                while not s[j].isalnum():
                    j -= 1
                if s[i].lower() != s[j].lower():
                    return False
                j -= 1
            i += 1
        
        return True