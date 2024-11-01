class Solution(object):
    def evalRPN1(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        nums = []

        for token in tokens:
            if token == '+':
                nums.append(nums.pop() + nums.pop())
            elif token == '-':
                r, l = nums.pop(), nums.pop()
                nums.append(l - r)
            elif token == '*':
                nums.append(nums.pop() * nums.pop())
            elif token == '/':
                r, l = nums.pop(), nums.pop()
                nums.append(int(float(l) / float(r)))
            else:
                nums.append(int(token))
        
        return nums[0]
    
    def evalRPN2(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        def stacker():
            token = tokens.pop()

            if token not in '+-*/':
                return int(token)
            
            r = stacker()
            l = stacker()

            if token == '+':
                return l + r
            elif token == '-':
                return l - r
            elif token == '*':
                return l * r
            elif token == '/':
                return int(float(l) / r)
        
        return stacker()