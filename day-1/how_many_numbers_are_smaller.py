class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsort = sorted(nums)
        less = {}
        for index, num in enumerate(numsort):
            if num not in less:
                less[num] = index
        return [less[num] for num in nums]
