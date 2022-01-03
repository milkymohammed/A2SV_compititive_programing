class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums)-1:
            sum += nums[i]
            i += 2
        return sum
