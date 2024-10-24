# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example 1:
```plaintext
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:
```plaintext
Input: nums = [1], k = 1
Output: [1]
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.
  
## Solution

```python
# solution.py

def groupAnagrams1(self, strs): # solution 1
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    seen = dict()

    # O(n), where n is the length of the list
    for word in strs:
        # O(slogs) since join functionn is O(n) and the complexity is dominated by sorting
        # s is the length of the word
        w = ''.join(sorted(word))

        if w in seen:
            seen[w].append(word)
        else:
            seen[w] = [word]            
    
    return list(seen.values())
```

```python
# solution.py

def groupAnagrams2(self, strs): # solution 2
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    seen = {}

    for word in strs: # O(n)
        key = [0]*26 # O(1)

        for c in word: # O(s)
            key[ord(c) - ord('a')] += 1

        key = tuple(key) # O(1)

        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]

    return list(seen.values())
```

## Explanation
Complexity

Time: O(n*slogs)

Space: O(n)

By sorting each word, we can make it as a unique key string for the dictionary to store and categorize the same anagrams together.

Complexity

Time: O(n*s)

Space: O(n)

For each word, we make its list embedding by subtracting the unicode of 'a' from each character of the word to make it into an integer value within 0-25 for an index of the embedding. Then add the count on to the embedding. So each embedding is going to be 26x1 list with values representing how many the corresponding alphabet showed up in the word. The anagrams will have the same embedding so we can cluster them together.

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