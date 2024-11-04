# [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)


## Problem Description

You are given the `head` of a linked list, and an integer `k`.

Return the `head` of the linked list after swapping the values of the `kth` node from the beginning and the `kth` node from the end (the list is 1-indexed).

![Description](./desc.jpeg)

### Example 1:
```plaintext
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

### Example 2:
```plaintext
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

### Constraints:
- The number of nodes in the list is `n`.
- `1 <= k <= n <= 10^5`
- `0 <= Node.val <= 100`

## Solution

```python
# solution.py

def swapNodes(self, head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    l, r = None, head
    current = head
    n = 1

    while current:
        if n == k:
            l = current
        if n > k:
            r = r.next
        current = current.next
        n += 1
    
    l.val, r.val = r.val, l.val
    return head
```

## Explanation
Complexity

Time: O(n)

Space: O(1)

We iteratively find the nodes being swapped. `k-th` is when `i==k`, and `k-th` from the back is when `i==n-k+1`, which can be also found by traversing `r` pointer `k-iterations` after `l` pointer. Then we swap the values.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)