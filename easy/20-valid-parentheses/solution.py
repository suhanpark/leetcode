class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) % 2 != 0: return False

        stack = []
        closers = { '}': '{',
                    ')': '(',
                    ']': '['}

        for i, c in enumerate(s):
            if c in closers:
                if stack and stack[-1] == closers[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return not stack
        