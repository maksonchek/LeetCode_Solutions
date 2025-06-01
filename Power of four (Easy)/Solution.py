class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 4
        if n == num:
            return True
        elif n < num:
            if n == 1:
                return True
            return False
        while num < n:
            num = num*4
            if num == n:
                return True
        return False
        
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()
        