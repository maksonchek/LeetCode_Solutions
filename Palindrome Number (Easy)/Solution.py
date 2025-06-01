class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new = 0
        orig = x
        while x:
            num = x%10
            x = x//10
            new = new*10 + num
        return new == orig