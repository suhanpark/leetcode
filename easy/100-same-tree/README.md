# [100. Same Tree](https://leetcode.com/problems/same-tree/description/)


## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

![Description 1](./desc1.png)

### Example 1:
```plaintext
Input: p = [1,2,3], q = [1,2,3]
Output: true

```
![Description 2](./desc2.png)

### Example 2:
```plaintext
Input: p = [1,2], q = [1,null,2]
Output: false
```
![Description 3](./desc3.png)

### Example 3:
```plaintext
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

### Constraints:
- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`


## Solution

```python
# solution.py

def isSameTree(self, p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """
    def dfs(node1, node2):
        if not node1 and not node2:
            return True
        
        if (not node1 and node2) or (node1 and not node2):
            return False
        
        if node1.val != node2.val:
            return False
        
        return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

    return dfs(p, q)
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform depth-first-search, then check if each node from both trees are the same.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)