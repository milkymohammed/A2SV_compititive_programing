class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for temp in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                n = stack.pop()
                ans[n] = i - n       
            stack.append(i)
            
            
        return ans
