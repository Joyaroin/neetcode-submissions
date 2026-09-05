class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for n in strs:  
            res += str(len(n)) + "#" + n
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1 
            res.append(s[start:start + length])
            i = start + length
        return res
