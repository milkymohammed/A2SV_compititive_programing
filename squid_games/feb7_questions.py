#### Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            if i == "./":
                pass
            elif i=="../":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(i[0:len(i)-1])
                
        return len(stack)
   
  
#### Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]


####  Robot Bounded In Circle
      
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr_point = [0,0]
        direction = 'up'
        change_dir = {'up_L':'left','left_L':'down','down_L':'right','right_L':'up',
                    'up_R':'right','right_R':'down','down_R':'left','left_R':'up'}
        move_toward = {'up':[0,1],'right':[1,0],'down':[0,-1],'left':[-1,0]}
        
        for c in instructions:
            if c != 'G':
                direction = change_dir[direction+'_'+c]
            else:
                curr_point = list(map(lambda a,b:a+b, curr_point, move_toward[direction]))

        return True if curr_point == [0,0] or direction !='up' else False

      
##### Text Justification
      
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        lines = defaultdict(list)
        lengths = defaultdict(int)
        count = 0
        width = maxWidth
        
        for i in range(n):
            word = words[i]
            m = len(word) 
            if m > width:
                width = maxWidth
                count += 1
            lines[count].append(word)
            lengths[count] += m
            width = width - (m + 1)

        result = []
        l = len(lines)
        for key, values in enumerate(lines.values()):
            spaces = len(values) - 1
            width = maxWidth - lengths[key]
            s = ''
            if key == l - 1:
                for i, v in enumerate(values):
                    if i == spaces:
                        s += v.ljust(width + len(v))
                    else:
                        s += v + ' '
                        width -= 1
            elif spaces == 0:
                s = values[0].ljust(maxWidth)
            else:
                for i in range(spaces, -1, -1):
                    s = values[i] + s
                    if i > 0:
                        s = ' ' * (width // i) + s
                        width = width - (width // i)
            result.append(s)
                
        return result
