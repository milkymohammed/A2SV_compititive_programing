### Bus Routes

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        set_routes = [set(route) for route in routes]
        start_buses = [i for i, s in enumerate(set_routes) if source in s]
        state = set()

        for i in start_buses[::-1]:
            state.update(set_routes.pop(i))
        if target in state:
            return 1

        n_buses = 1
        while state:
            new_state = set()
            n_buses += 1
            new_busses = [i for i, s in enumerate(set_routes) if state & s]
            for i in new_busses[::-1]:
                new_state.update(set_routes.pop(i))
            if target in new_state:
                return n_buses
            state = new_state
            
        return -1
      
      
 ### Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        i = set(nums)
        i = list(i)

        if len(i) < 3:
            return max(i)
        else:
            i.sort(reverse=True)
            return i[3-1]
          
          
  #### Restore the Array From Adjacent Pairs
  
  class Solution:
      def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        union, hashmap = defaultdict(list), defaultdict(int)
        for i, j in adjacentPairs: union[i].append(j); union[j].append(i)
        for i, j in adjacentPairs: hashmap[i] += 1; hashmap[j] += 1   
        for i, j in hashmap.items(): 
            if j == 1: node = union[i][0]; lst = [i, node]

        while True:
            if union[node][0] != lst[-2]: lst.append(union[node][0])
            elif len(union[node]) == 2: lst.append(union[node][1])
            else: break
            node = lst[-1]
        return lst
      
 #### Evaluate Division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for e, v in zip(equations, values):
            a,b = e 
            graph[a].append((b,v))
            graph[b].append((a,1/v))
            
        result = []
        
        for query in queries:
            find = False 
            visited = set()
            a, b = query[0], query[1]
            if a not in graph:
                result.append(-1)
                continue
            q = collections.deque([(a,1)])

            while q:
                start,val = q.popleft()        
                if start == b:
                    result.append(val)
                    find = True 
                    break
                visited.add(start)
                for end,v in graph[start]:
                    if end not in visited:
                        q.append((end,val * v))
            if find: continue 
            else: result.append(-1)
            
        return result
