# [167. Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

### Example 1:
```plaintext
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

### Example 2:
```plaintext
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

### Example 3:
```plaintext
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

### Constraints:
- `2 <= numbers.length <= 3 * 10^4`
- `1000 <= numbers[i] <= 1000`
- numbers is sorted in non-decreasing order.
- `1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.
  
## Solution

```python
# solution.py

def twoSum1(self, numbers, target): # solution 1
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    nums = {n: i for i, n in enumerate(numbers)}

    for i, n in enumerate(numbers):
        diff = target - n
        if diff in nums and nums[diff] != i:
            return [min(nums[diff], i)+1, max(nums[diff], i)+1]
    
    return []
```

```python
# solution.py

def twoSum2(self, numbers, target): # solution 2
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    l, r = 0, len(numbers)-1
    
    while numbers[l]+numbers[r] != target:
        if numbers[l]+numbers[r] > target:
            r -= 1
        elif numbers[l]+numbers[r] < target:
            l += 1
        
    return [l+1, r+1]
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

Since the list is sorted, we make a hashmap of the numbers in order to have O(1) lookup. Then we linearly loop through the list and check if the complement is in the hashmap. Now, this solution is computationally costly since we have to make a lookup table.

Complexity

Time: O(n)

Space: O(1)

Since we know the list is sorted, we can use this concept: `numbers[i] <= numbers[i+1]`. We can set two pointers (`l` and `r`) one in the beginning and one at the end of the list to start with. Then, we loop until we find two indices that their elements add up to the `target`. Here, we should know that if the current sum is larger than the `target` then we have to decrease the larger number, which is `r`, if it's smaller, then increase the smaller number, which is `l`. Then return the final list of indices.

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