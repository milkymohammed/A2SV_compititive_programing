class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st_s = list()
        st_t = list()
        
        for c in s:

            if not st_s and c == '#':
                continue
                
            elif c == '#':
                st_s.pop()
                
            else:
                st_s.append(c)
        
        for c in t:
            
            if not st_t and c == '#':
                continue
                
            elif c == '#':
                st_t.pop()
                
            else:
                st_t.append(c)
                
        
        return ''.join(st_s) == ''.join(st_t)
