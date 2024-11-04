# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)


## Problem Description

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its `head`.

![Description](./desc.jpg)

### Example 1:
```plaintext
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:
```plaintext
Input: head = [1], n = 1
Output: []
```

### Example 3:
```plaintext
Input: head = [1,2], n = 1
Output: [1]
```

### Constraints:
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

Follow up: Could you do this in one pass?

## Solution

```python
# solution.py

def removeNthFromEnd(self, head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    if not head.next and n == 1:
        head = None
        return head

    current = head
    l = head
    i = 0
    while current:
        if i > n:
            l = l.next
        i += 1
        current = current.next

    if i == n:
        return head.next

    l.next = l.next.next

    return head
```

## Explanation
Complexity

Time: O(n)

Space: O(1)

We find the very last node before the node being removed, `l`, then set the next node (target node)'s next node to be the node (`l`)'s next. There're edge cases where the head is being removed, which we find it by comparing the length of the list and `n`. Then return the next node.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)