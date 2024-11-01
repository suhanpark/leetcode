# [15. 3Sum](https://leetcode.com/problems/3sum/description/)


## Problem Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.


### Example 1:
```plaintext
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

### Example 2:
```plaintext
Input: nums = [0,1,1]
Output: []
```

### Example 3:
```plaintext
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

### Constraints:
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Solution

```python
# solution.py

def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    result = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        j, k = i+1, len(nums)-1
        
        while j < k:
            s = n + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                last = [n, nums[j], nums[k]]
                result.append(last)

                j += 1
                while nums[j] == nums[j -1] and j < k:
                    j += 1
        
    return result
```

## Explanation
Complexity

Time: O(n^2)

Space: O(1)

We utilize the solution for 2-sum problem. We check the sum for every n in the sorted list, then perform 2-sum. Note that we increment the pointer `j` to skip the same element. 

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)