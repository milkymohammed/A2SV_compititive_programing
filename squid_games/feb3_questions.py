##### Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        n = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[n]:
                t1 = s[:i] + s[i+1:]
                t2 = s[:n] + s[n+1:]
                if t1 == t1[::-1] or t2 == t2[::-1]:
                    return True
                break
            n -= 1
            
        return False
      
#### Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return "/"
        
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or not part:
                continue
            else:
                stack.append(part)
        tot = "/" + "/".join(stack)
        
        return tot
      
#### Random Pick with Weight
      
 class Solution:
    def __init__(self, w: List[int]): 
        for i in range(1, len(w)): w[i] += w[i - 1]    
        self.w = w

    def pickIndex(self) -> int:
        point = random.randint(1, self.w[-1])
        l = 0
        r = len(self.w) - 1
        index = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.w[mid] == point:  return mid
            if self.w[mid] < point:
                l = mid + 1
            else: r = mid - 1
        
        return l
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

#### Vertical Order Traversal of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        def dfs(node, a, b):
            dic[a].append([b, node.val])
            if node.left: dfs(node.left, a-1, b+1)
            if node.right: dfs(node.right, a+1, b+1)
        dfs(root, 0, 0) 

        return [[v[1] for v in sorted(dic[k])] for k in sorted(dic)]
