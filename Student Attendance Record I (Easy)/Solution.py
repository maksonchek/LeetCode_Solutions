class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i, n in enumerate(s):
            if n == 'A':
                a += 1
            if (i < len(s)-1) and i > 0:
                if (n == 'L') and (s[i+1] == 'L') and s[i-1] == 'L':
                    l = 1
        if a < 2 and l == 0:
            return True
        else:
            return False