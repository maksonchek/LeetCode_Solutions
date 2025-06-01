class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def d_num(num):
            ret = 0
            while num:
                num//=10
                ret += 1
            return ret
        ans = 0
        for num in nums:
            ans += int(d_num(num)%2==0)
        return ans