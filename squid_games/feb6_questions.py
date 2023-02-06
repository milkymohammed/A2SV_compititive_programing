### Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        l = len(pref)
        for i in words:
            if l <= len(i):
                if pref == i[:l]:
                    res += 1
        return res
      
### Longest String Chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = {}
        words.sort(key = lambda x : len(x))
        for i, w in enumerate(words):
            dic[w] = i

        dp = [1 for _ in words]
        for i in range(1, len(words)):
            w = words[i]
            for j in range(len(w)):
                if (e := w[ : j] + w[j + 1 : ]) in dic:
                    dp[i] = max(dp[i], 1 + dp[dic[e]])
                    
        return max(dp)


 #### Detect Squares

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = {}
        words.sort(key = lambda x : len(x))
        for i, w in enumerate(words):
            dic[w] = i

        dp = [1 for _ in words]
        for i in range(1, len(words)):
            w = words[i]
            for j in range(len(w)):
                if (e := w[ : j] + w[j + 1 : ]) in dic:
                    dp[i] = max(dp[i], 1 + dp[dic[e]])
                    
        return max(dp)
      
###  Race Car
      
class Solution:
    def racecar(self, target: int) -> int:
        moll = deque([[0,0,1]])
        visited = set()
        
        while moll:
            move,position,speed = moll.popleft()
            if position==target:
                return move
            if (position,speed) in visited: continue

            visited.add((position,speed))
            moll.append([move+1,position+speed,speed*2])
            if (position+speed>target and speed>0) or (position+speed<target and speed<0):
                speed = -1 if speed>0 else 1
                moll.append([move+1,position,speed])
      
