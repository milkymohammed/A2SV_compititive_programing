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


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def f(A):
            n = len(A)
            a = [set() for _ in range(n+1)]
            a[0].add(0)

            for i in A:
                for j in range(n,0,-1):
                    for v in a[j-1]:
                        a[j].add(v+i)

            return list(map(sorted, a))


        s = sum(nums)
        n = len(nums)
        a = f(nums[:n//2])
        b = f(nums[n//2:])
        res = float('inf')

        for i in range(n//2+1):
            j = len(b[n//2-i]) - 1
            for v in a[i]:
                while j >= 0 and v + b[n//2-i][j] > s // 2:
                    j -= 1
                if j >=0:
                    res = min(res, s - 2 * (v+b[n//2-i][j]))
                    
        return res
Console

