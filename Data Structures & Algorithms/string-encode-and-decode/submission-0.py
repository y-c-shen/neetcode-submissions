import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"%{len(s)}%{s}")
        print("".join(res))   
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        find_pattern = r"%\d+%"
        parts = re.split(find_pattern, s)
        print(parts)
        return parts[1:]



