# [1. Two Sum](https://leetcode.com/problems/two-sum/description/)


## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


### Example 1:
```plaintext
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

### Example 2:
```plaintext
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```plaintext
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

## Solution

```python
# solution.py

def twoSum(self, nums, target):
    seen = {}

    for i, n in enumerate(nums):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        
        seen[n] = i

```

## Explanation
Complexity

Time: O(n)

Space: O(n)

The concept of this approach is to check if the complement has been seen, so the algorithm doesn't have to check back for the same number again.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)