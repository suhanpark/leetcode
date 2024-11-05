# [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/description/)


## Problem Description

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

![Description 1](./desc1.jpeg)

### Example 1:
```plaintext
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
```

![Description 2](./desc2.jpeg)

### Example 2:
```plaintext
Input: root = [2,1,3]
Output: [2,1,3]
```

### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 10^5`


## Solution

```python
# solution.py

def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    tree = []
    
    def dfs(node):
        if not node: return

        dfs(node.left)
        tree.append(node.val)
        dfs(node.right)

    def percolate(left, right):
        if left > right: return None

        mid = (left + right) // 2
        return TreeNode(tree[mid], percolate(left, mid-1), percolate(mid+1, right))

    dfs(root)

    return percolate(0, len(tree)-1)
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform inorder traversal to keep the nodes in order in the array `tree`. Then we percolate nodes recursively starting from the mid value of the array.


## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)