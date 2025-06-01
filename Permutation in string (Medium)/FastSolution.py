class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, s1_len = Counter(s1), len(s1)
        matched = 0
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1

            if i >= s1_len and s2[i-s1_len] in cntr:
                if cntr[s2[i-s1_len]] == 0:
                    matched -= 1
                cntr[s2[i-s1_len]] += 1

            if matched == len(cntr):
                return True
        return False