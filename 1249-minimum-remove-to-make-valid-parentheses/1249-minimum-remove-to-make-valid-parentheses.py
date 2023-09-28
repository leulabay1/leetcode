class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = list(s)
        stack = []
        n = len(s)
        brackets = '()'
        
        for ii in range(n):
            if s[ii] not in brackets:
                continue
                
            if s[ii] == '(':
                stack.append(ii)
            else:
                if not stack:
                    valid[ii] = ''
                else:
                    stack.pop()
        
        while stack:
            valid[stack.pop()] = ''
        
        return ''.join(valid)