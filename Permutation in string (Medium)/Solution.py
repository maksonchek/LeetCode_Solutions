class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        d_s1 = {}
        for s in s1:
            d_s1[s] = d_s1.get(s, 0) + 1
        if len(s2) == 1:
            if len(s1) == 1:
                if s1 == s2:
                    return True
                else:
                    return False
            else:
                return False
        if len(s1) == 1:
            if len(s2) == 1:
                if s1 == s2:
                    return True
                else:
                    return False
            else:
                return s1 in s2

        while r < len(s2):
            if s2[r] not in d_s1:
                l = r
                r += len(s1) - 1
            else:
                if s2[l] not in d_s1:
                    l += 1
                    r += 1
                else:
                    cntr = {}
                    for i in range(l, r+1):
                        if s2[i] not in d_s1:
                            break
                        cntr[s2[i]] = cntr.get(s2[i], 0) + 1
                    if cntr == d_s1:
                        return True
                    else:
                        l += 1
                        r += 1
        return False
