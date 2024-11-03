class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ln = len(temperatures)
        result = [0]*ln
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, j = stack.pop()
                result[j] = i - j
            stack.append((t, i))

        return result