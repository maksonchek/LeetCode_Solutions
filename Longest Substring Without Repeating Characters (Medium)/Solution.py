class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dict = {}
        l = 0
        for r in range(len(s)):
            dict[s[r]] = dict.get(s[r], 0) + 1
            while max(dict.values()) > 1:
                dict[s[l]] -= 1
                l += 1
            if max_len < r-l + 1:
                max_len = r-l+1
        return max_len