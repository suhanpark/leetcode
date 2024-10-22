# [NC. Duplicate Integers](https://neetcode.io/problems/duplicate-integer)


## Problem Description

Given two strings s and t, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:
```plaintext
Input: s = "racecar", t = "carrace"
Output: true
```

### Example 2:
```plaintext
Input: s = "jar", t = "jam"
Output: false
```


### Constraints:
- s and t consist of lowercase English letters.

## Solution

```python
# solution.py

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    sd, td = dict(), dict()

    for i in range(len(s)):
        if s[i] in sd:
            sd[s[i]] += 1
        else:
            sd[s[i]] = 1
        
        if t[i] in td:
            td[t[i]] += 1
        else:
            td[t[i]] = 1
        
    return sd == td 

```

## Explanation
Complexity

Time: O(n)

Space: O(2n) -> O(n)

Consider anagram can have different order of characters, but have to contain the same characters.
We want to record how many each character is in each list and compare the dictionaries to show the two are anagram.
