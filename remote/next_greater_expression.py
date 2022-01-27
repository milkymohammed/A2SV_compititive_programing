class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        
        for n in nums2:
            
            while(stack and n > stack[-1]):
                c = stack.pop()
                m[c] = n
            
            stack.append(n)
        
        return [m.get(n, -1) for n in nums1]
