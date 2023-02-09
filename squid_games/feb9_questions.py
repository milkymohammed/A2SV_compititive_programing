Subarrays with K Different Integers

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def at_most_k(k: int) -> int:
            beg=0
            count=Counter()
            res=0

            for end in range(n):
                if count[(e := nums[end])] == 0:
                    k -= 1
                count[e] += 1

                while k < 0:
                    count[(s := nums[beg])] -= 1
                    if count[s] == 0:
                        k += 1
                    beg += 1    
                res += end - beg + 1

            return res
            
        return at_most_k(k) - at_most_k(k - 1)
      
      
      Reformat Date
      
  def reformatDate(self, date: str) -> str:
        m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split()
        d = date[-3][:-2] if int(date[-3][:-2]) >= 10 else '0'+date[-3][:-2]
        m = m.index(date[-2])+1 if (m.index(date[-2])+1) >= 10 else '0'+str(m.index(date[-2])+1)
        return f'{date[-1]}-{m}-{d}'
      
      
      Restore IP Addresses
      
      
 class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if s == "":
           return []
        self.rs = []
        self.ln = len(s)
        self.s = s
        self.helper(0, 0, "")
        return self.rs

    def helper(self, part, idx, tmp):
        if part < 4 and idx < self.ln:
            for i in range(idx, min(idx+3, self.ln)):
                nm = self.s[idx: i+1]
                if 0 <= int(nm) <= 255 and (i == idx or nm[0] != '0'):
                    self.helper(part+1, i+1, tmp + nm + ".")
        elif part == 4 and idx == self.ln:
            self.rs.append(tmp[:-1]) 
            
            
            Maximum Swap
            
            
  class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int,str(num)))
        n = len(num)
         
        maxs = deque()
        for i in range(n-1,-1,-1):
            maxs.appendleft(max(maxs[0],i,key=lambda i: num[i]) if maxs else i)
            
        for i in range(n):
            if num[maxs[i]]>num[i]:
                num[maxs[i]],num[i]= num[i],num[maxs[i]]
                return int("".join(map(str,num)))
        
        return int("".join(map(str,num)))
      
      
      
      
