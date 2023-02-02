####Make Array Zero by Subtracting Equal Amounts

  def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        while nums != [0]*n:
            count += 1
            small = min([i for i in nums if i > 0])
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= small
                    
        return count
      
 #### Number of Ways to Select Buildings

 class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = len(s) - zeros
        zeroPrefix = onePrefix = res = 0
        for c in s:
            if c == '0':
                res += onePrefix * (ones - onePrefix)
                zeroPrefix += 1
            else:
                res += zeroPrefix * (zeros - zeroPrefix)
                onePrefix += 1
        
        return res
      
      
      
#### Reorder Data in Log Files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLogs = []
        digLogs = []
        
        for log in logs:
            curLog = log.split(" ", 1)
            if curLog[1][0].isdigit():
                digLogs.append(log)
            else:
                letLogs.append((curLog[1], curLog[0]))
                
        letLogs.sort()
               
        return [" ".join([log[1], log[0]]) for log in letLogs] + digLogs
      
      
 #### Integer to English Words

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0 : return 'Zero' 
        d = {1000000000 : 'Billion',1000000 : 'Million',1000 : 'Thousand',100 : 'Hundred', 
		90:'Ninety',80:'Eighty',70:'Seventy',60:'Sixty',50: 'Fifty', 40 : 'Forty', 30 : 'Thirty', 20 : 'Twenty',
		19 :'Nineteen',18 :'Eighteen',17:'Seventeen',16:'Sixteen',15:'Fifteen',14:'Fourteen',13:'Thirteen',12:'Twelve',11:'Eleven',
		10:'Ten',9:'Nine',8:'Eight',7:'Seven',6:'Six',5:'Five',4:'Four',3:'Three',2:'Two',1:'One'} 
        ans = ""                      
        for key, value in d.items():  
            if num//key>0 :           
                x = num//key          
                if key >= 100 :       
                    ans += self.numberToWords(x) + ' '
                ans  += value + " "
                num = num%key         
        return ans.strip()
