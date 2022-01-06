class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        
        for number in range(1, len(nums)):
            if nums[number] != nums[number - 1]:
                nums[unique] = nums[number]
                unique += 1
        return unique
        
