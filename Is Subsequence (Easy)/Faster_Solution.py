class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_i = 0
        for t_i, char in enumerate(t):
            if char == s[s_i]:
                s_i += 1

            if s_i == len(s):
                return True

        return False