class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        z = 0
        max_ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z+=1
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l+=1
            ans = r-l+1-z

            max_ans = max(max_ans,ans)
        if max_ans == len(nums):
            return max_ans - 1
        else:
            return max_ans

            