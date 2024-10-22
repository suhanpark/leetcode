# [88. Merge Sorted Arrays](https://leetcode.com/problems/merge-sorted-array/description/)


## Problem Description

```markdown
You are given two integer arrays `nums1` and `nums2`, 
sorted in non-decreasing order, and two integers `m` and `n`, 
representing the number of elements in `nums1` and `nums2` respectively.

The task is to merge `nums1` and `nums2` into a single array sorted in non-decreasing order. 
The final sorted array should not be returned by the function but instead be stored inside `nums1`. 
To accommodate this, `nums1` has a length of `m + n`, 
where the first `m` elements denote the elements that should be merged, 
and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.
```

### Example 1:
```plaintext
Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]
```

### Example 2:
```plaintext
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

### Example 3:
```plaintext
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

### Constraints:
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Solution

```python
# solution.py

def merge(nums1, m, nums2, n):
    p1, p2, p3 = m-1, m+n-1, n-1

        while p3 >= 0:
            if  p1 >= 0 and nums1[p1] > nums2[p3]:
                nums1[p2] = nums1[p1]
                p1 -= 1 
            else:
                nums1[p2] = nums2[p3]
                p3 -= 1
                
            p2 -= 1

```

## Explanation
Complexity
Time: O(n)
Space: O(1)

Consider the 3 pointers that point to
  1. End of nums1 (p1)
  2. End of where original values of nums1 are (p2)
  3. End of nums2 (p3)

We will stop updating the list when p3 is less than 0 (when it hits the beginning of nums2).
Then we're going to update the element at p1 in nums1 with when:
  1. p1 is within the bounds of nums1
  2. the number trying to insert is larger than the originally stored value

Then we additionally decrement p1 to move left and point smaller element.
We will update the elements in nums1 that are within the index range of initial p1 and end of p1
when the number in nums1 is smaller or equal to nums2 (it will be since it's 0).
Then we insert the number from nums2 and decrement p3 to move left and point smaller element.

Every iteration we decrement p2 to move left and point smaller element in nums1.


## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)

