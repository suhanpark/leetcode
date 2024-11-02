class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append(''.join(stack))
                return
            
            if open_n > closed_n:
                stack.append(')')
                backtrack(open_n, closed_n+1)
                stack.pop()
            
            if open_n < n:
                stack.append('(')
                backtrack(open_n+1, closed_n)
                stack.pop()

        backtrack(0, 0)
        return result