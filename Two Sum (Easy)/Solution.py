class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            dev = target - num
            if dev in d:
                return [d[dev], i]
            d[num] = i
        