# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)


## Problem Description

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


### Example 1:
```plaintext
Input: s = "()"
Output: true
```

### Example 2:
```plaintext
Input: s = "()[]{}"
Output: true
```

### Example 3:
```plaintext
Input: s = "(]"
Output: false
```

### Example 4:
```plaintext
Input: s = "([])"
Output: true
```

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `()[]{}`.

## Solution

```python
# solution.py

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

```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We stack each opening brackets and if we have closing bracket, we check if the top of the stack is matching pair, then pop if it is. At the end we check if the stack is empty.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)