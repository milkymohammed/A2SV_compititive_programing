class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            
            if i == 'D':
                m = int(stack.pop())
                stack.extend([m,2*m])
                
            elif i == 'C':
                stack.pop()
                
            elif i == '+':
                m = int(stack.pop())
                n = int(stack.pop())
                stack.extend([n,m,m+n])
                
            else:
                stack.append(int(i))

        return sum(stack)
