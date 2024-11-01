# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

## Problem Description

You are given an array of strings tokens that represents an arithmetic expression in a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are `+`, `-`, `*`, and `/`.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

### Example 1:
```plaintext
Input: tokens = ["2","1","+","3","*"]
Output: 9
```

### Example 2:
```plaintext
Input: tokens = ["4","13","5","/","+"]
Output: 6
```

### Example 3Sum:
```plaintext
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

### Constraints:
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.
  
## Solution

```python
# solution.py

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
```

```python
# solution.py

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
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We keep appending numbers to the stack until we find an operator. Once we find one, we pop the numbers from stack to have operands. Then we calucate and append the result. We repeat this until the end of the stack. Then return the number.

Complexity

Time: O(n)

Space: O(n)

We recursively call the inner function to retrieve elements at the top of the stack. Then we return the result which will be stacked by recursive call stacks until we finally return the final result.

## Results

The following graphs show the performance of the solution:

### Time Complexity 1
![Time Complexity](./time1.png)

### Memory Usage 1
![Memory Usage](./space1.png)

### Time Complexity 2
![Time Complexity](./time2.png)

### Memory Usage 2
![Memory Usage](./space2.png)