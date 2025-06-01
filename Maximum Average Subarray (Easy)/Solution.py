class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])/k
        max_avg = avg
        for i in range(k, len(nums)):
            avg = avg + (nums[i] - nums[i-k])/k
            if avg > max_avg:
                max_avg = avg
        return max_avg
            