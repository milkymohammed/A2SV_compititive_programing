### Squares of a Sorted Array

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mid = 0
        l = mid - 1
        r = mid
        ans = []
        for i in range(n):
            if nums[i] >= 0:
                mid = i
                break
            else:
                mid = n-1
        
        while l >= 0:
            if l < r:
                ans.append(nums[l])
                l -= 1
        while r < n:
            if l > r:
                ans.append(nums[r])
                r += 1
        return ans
        
 
 ### Median of Two Sorted Arrays
 
  class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        L = len(nums1)
        
        if L%2==1:
            return nums1[((L-1)//2)]
        else:
            return (nums1[L//2-1]+nums1[L//2])/2
            
    
    ### Image Overlap
    
    class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l = len(img1)                   
        
        p1, p2 = [], []                 
        for r in range(l):
            for c in range(l):
                if img1[r][c] == 1:
                    p1.append((r,c))
                if img2[r][c] == 1:
                    p2.append((r,c))
        
        d = {None: 0}                   
        for r1, c1 in p1:
            for r2, c2 in p2:
                v = (r1-r2, c1-c2)      
                if v not in d:
                    d[v] = 1
                else:
                    d[v] += 1
        return max(d.values())   
        
        
   #### Number of Pairs of Strings With Concatenation Equal to Target
        
        
   class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c= 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]== target and i!= j:
                    c+= 1

        return c
