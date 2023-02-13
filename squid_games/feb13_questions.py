####   Shortest Path in Binary Matrix
  
  
  class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        if grid[0][0] == 1:
            return -1

        q = [(0, 0, 1)]
        while len(q) > 0:
            x, y, d = q.pop(0)
            if x == r-1 and y == c-1:
                return d
                
            for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
                if 0 <= a < r and 0 <= b < c and grid[a][b] == 0:
                    grid[a][b] = 1
                    q.append((a, b, d+1))
        
        return -1\
      
      
      
      
      
        count = 0
        s = 0
        sum_map = {}
        for i in nums:
            s+=i 
            s= s%k
            if s in sum_map:
                sum_map[s]+=1
            else:
                sum_map[s] = 1

        for i in sum_map:
            su = sum_map[i]
            if i==0:
                count = count + (su*(su -1))//2 + su
            else:
                count += (su*(su -1))//2
        return count
