# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)


## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


![Description](./desc.png)

### Example 1:
```plaintext
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

### Example 2:
```plaintext
Input: height = [4,2,0,3,2,5]
Output: 9
```

### Constraints:
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Solution

```python
# solution.py

def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height: return 0

    l, r = 0, len(height) - 1
    max_l, max_r = height[l], height[r]
    a = 0

    while l < r:
        if height[l] < height[r]:
            if height[l] <= max_l:
                a += max_l - height[l]
                l += 1
            else:
                max_l = height[l]
                l += 1
        else:
            if height[r] <= max_r:
                a += max_r - height[r]
                r -= 1
            else:
                max_r = height[r]
                r -= 1
    return a
```

## Explanation
Complexity

Time: O(n)

Space: O(1)

We constantly keep track on the maximum height of left bar and right bar to calculate the water trapped for each point.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)