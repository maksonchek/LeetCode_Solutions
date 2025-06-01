class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        if s == "":
            return True
        if not s:
            return False
        for f in range(len(t)):
            if t[f] == s[l]:
                if l < len(s)-1:
                    l+=1
                else:
                    return True
        return False
