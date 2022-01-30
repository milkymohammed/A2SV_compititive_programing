class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def isnum(s):
            try:
                int(s)
                return True
            except:
                return False
            
            
        for i in tokens:
            if isnum(i):
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                
                if i == "+":
                    c = b+a
                elif i == "-":
                    c = b-a
                elif i == "*":
                    c = b*a 
                elif i== "/":
                    c = int(b/a)
                stack.append(str(c))
                    
        return stack[-1]
                
        
