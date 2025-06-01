class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = num
        r = num
        l_prev = 0
        r_prev = 0
        while (l,r) != (l_prev, r_prev):
            l_prev = l
            r_prev = r
            if l**2 == num:
                return True
            elif l**2 < num:
                l = (r+l)//2
            elif l**2 > num:
                r = l
                l = l//2
        return False