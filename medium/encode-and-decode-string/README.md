# [Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode)


## Problem Description

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.


### Example 1:
```plaintext
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
```

### Example 2:
```plaintext
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
```


### Constraints:
- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters.


## Solution

```python
# solution.py

def encode(self, strs: List[str]) -> str:
    encoded = ''

    for s in strs: # O(n), where n is the length of the list
        l = str(len(s)).zfill(3) # O(m), where m is the length of the longest string
        encoded += f'**{l}{s}'

    return encoded
    
def decode(self, s: str) -> List[str]:
    decoded = []
    
    i = 0
    while i < len(s): # O(n)
        key = int(s[i:i+5][2:])
        decoded.append(s[i+5:i+5+key])
        i += 5 + key
    
    return decoded
```

## Explanation
Complexity

Time: O(n*m)

Space: O(n)

We add an encoding string `**` followed by the length of the string. Then we decode using the indicator and the length of the string to slice.
