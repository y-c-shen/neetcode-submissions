class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in "[({":
                stk.append(c)
            else:
                if not stk: return False
                elif c == ']' and stk[-1] == '[':
                    stk.pop()
                elif c == '}' and stk[-1] == '{':
                    stk.pop()
                elif c == ')' and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
        return len(stk) == 0
