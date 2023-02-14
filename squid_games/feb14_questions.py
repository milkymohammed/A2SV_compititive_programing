          class Solution:
  def minimumDeletions(self, s: str) -> int:
        stack = []
        count = 0
        
        for i in s:
            if stack and stack[-1] == 'b' and i == 'a':
                stack.pop()
                count += 1
            
            else:
                stack.append(i)
                
        return count
      
      
      
      class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i, arr = 0, []
        v = 2**i
        while v <= 10**9: arr.append(sorted(str(v))); i+=1; v = 2**i
        return sorted(str(n)) in arr
        
        
        
        class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n%2!=0:
            ans.append(0)

        for i in range(1,n//2+1):
            ans.append(-i)
            ans.append(i)

        return ans
