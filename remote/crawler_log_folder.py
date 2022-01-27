class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        stack.append(".")
        for operat in logs:
            
            if operat=="./":
                continue
            elif operat=="../":
                if len(stack)>1:
                    stack.pop()
            else:
                stack.append(operat)
        return len(stack)-1
