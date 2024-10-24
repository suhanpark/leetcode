from collections import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            l = str(len(s)).zfill(3)
            encoded += f'**{l}{s}'

        return encoded
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        
        i = 0
        while i < len(s):    
            key = int(s[i:i+5][2:])
            decoded.append(s[i+5:i+5+key])
            i += 5 + key
        
        return decoded
