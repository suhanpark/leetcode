# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example 1:
```plaintext
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:
```plaintext
Input: nums = [1], k = 1
Output: [1]
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.
  
## Solution

```python
# solution.py

def isPalindrome1(self, s): # solution 1
    """
    :type s: str
    :rtype: bool
    """
    
    s = re.sub(r'[^a-zA-Z0-9]', '', s) # O(n)
    
    for i in range(len(s)): # O(m)
        if s[i].lower() != s[-i-1].lower():
            return False
    
    return True
```

```python
# solution.py

def isPalindrome2(self, s): # solution 2
    """
    :type s: str
    :rtype: bool
    """
    
    i, j = 0, len(s)-1

    while i <= j: # O(n)
        if s[i].isalnum():
            while not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
        i += 1
    
    return True
```

## Explanation
Complexity

Time: O(2n) -> O(n)

Space: O(n)

By using regex, we can remove non-alphanumeric characters. Then we loop through to check if the opposite element is the same.

Complexity

Time: O(n)

Space: O(1)

By having a pointer on the left and on the right, we can update the pointers to skip non-alphanumeric characters.
So, we don't have to replace characters, nor we have to copy the string. 


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