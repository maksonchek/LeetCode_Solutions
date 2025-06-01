class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pref = 0
        d = {0:1}
        for num in nums:
            pref = pref + num
            if pref - k in d:
                ans += d[pref - k]
            if pref not in d:
                d[pref] = 1
            else:
                d[pref] = d[pref] + 1
        return ans

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = {0:1}
        pref = 0
        ans = 0
        for n in nums:
            if n + pref - k in prefs:
                ans += prefs[n + pref - k]
            pref += n
            prefs[pref] = prefs.get(pref, 0) + 1
        return ans