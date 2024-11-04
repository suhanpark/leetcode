# [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)


## Problem Description

Given the `root` of a binary search tree and an integer `k`, return `true` if there exist two elements in the BST such that their sum is equal to `k`, or `false` otherwise.

![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```
![Description 2](./desc2.jpg)

### Example 2:
```plaintext
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- `root` is guaranteed to be a valid binary search tree.
- `-10^5 <= k <= 10^5`


## Solution

```python
# solution.py

def findTarget(self, root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: bool
    """
    
    seen = set()

    def search(node):
        if not node: return False
        
        diff = k - node.val
        
        if diff in seen:
            return True
        else:
            seen.add(node.val)
            return search(node.right) or search(node.left) 

    return search(root)
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively check the sum by checking if the complement exist in each node. We keep track on difference by storing the values in hash set. 

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)