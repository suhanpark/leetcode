# [27. Remove Element](https://leetcode.com/problems/remove-element/description)

## Problem Description

```markdown
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, 
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return `k`.
```

### Example 1:
```plaintext
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

### Example 2:
```plaintext
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

### Constraints:
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
  

## Solution

```python
# solution.py

def removeElement(self, nums, val):
  count = 0

  for i in range(len(nums)):
      if nums[i] != val:
          nums[i], nums[count] = nums[count], nums[i]
          count += 1
  
  return count

```

## Explanation
Let the variable `count` be a pointer for swappable element and count for non-val-equal elements.
If we swap non-val-equal elements with "swappable" element (nums[count]) and increment the count,
then we will end up with a list that has val-equal elements clustered in the back of the list.


## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)

