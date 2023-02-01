 #### Minimum Recolors to Get K Consecutive Black Blocks
          
def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        res=[]

        for i in range(len(blocks)-k+1):
            res.append(blocks[l:k].count("W"))
            l+=1
            k+=1

        return min(res)
  
### Matrix Block Sum
        
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                result[i][j] = sum(sum(mat[x][max(0, j-k):min(n, j+k+1)])
                                   for x in range(max(0, i-k), min(m, i+k+1)))
                                   
        return result
        

#### Best Team With No Conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scoreage = sorted(zip(scores, ages))
        points = [0] * (max(ages) + 1)

        for score, age in scoreage:
            points[age] = max(points[: age + 1]) + score

            
        return max(points)
        
#### Earliest Possible Day of Full Bloom

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        couples = []
        res = start = 0
        
        for i in range(len(plantTime)):
            couples.append((growTime[i], plantTime[i]))
        
        couples.sort(reverse = True)

        for couple in couples:
            start += couple[1] 
            res = max(res, start + couple[0])
        
        return res
