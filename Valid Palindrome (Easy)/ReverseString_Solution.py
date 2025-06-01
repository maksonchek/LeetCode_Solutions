class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s if i.isalnum()]).lower()
        return all(s[i] == s[~i] for i in range(len(s)//2))


#https://leetcode.com/problems/valid-palindrome/solutions/3864359/python-3-two-solutions-beats-99-33ms