class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s_nums = sum(nums)
        s_range = sum(range(0, len(nums)+1))
        return s_range - s_nums