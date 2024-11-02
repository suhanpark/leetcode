# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)


## Problem Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Example 1:
```plaintext
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2:
```plaintext
Input: n = 1
Output: ["()"]
```


### Constraints:
- `1 <= n <= 8`

## Solution

```python
# solution.py

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
```

## Explanation
Complexity

Time: O((4^n)/sqrt(n))

Space: O(n)

We start with two lists, one for stacking the parentheses and another for collecting valid combinations. We define a inner function where it takes two arguments: number of open and closed parentheses (`open_n`, `closed_n`). Then, we perform backtracking following below conditions:
- if `n`, `open_n`, and `closed_n` are equal, then the combination is completed.
  - we append the combination to `result` and return to end the function call.
- if `open_n < n`, then we append `'('` then call `backtrack(open_n+1, closed_n)`. Pop the used parentheses after.
- if `open_n > closed_n`, then we append `')'` then call `backtrack(open_n, closed_n+1)`. Pop the used parentheses after.

Then we call the `backtrack()` function starting with `open_n=0` and `closed_n=0`.
Finally return the `result`.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)