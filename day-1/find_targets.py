class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        listo = []
        nums.sort()
        listo = [i for i, value in enumerate(nums) if value == target]
        return listo
