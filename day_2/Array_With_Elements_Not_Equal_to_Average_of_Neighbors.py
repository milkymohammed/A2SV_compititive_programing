class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        for i in range(len(nums)//2):
            arr.append(nums[i])
            arr.append(nums[len(nums)-i-1])
        if len(nums)%2 !=0:
            arr.append(nums[len(nums)//2])
        return arr
