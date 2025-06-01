class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for letter in s:
            res^=ord(letter)
        for letter in t:
            res^=ord(letter)
        return chr(res)
    
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sLetters = {}
        for c in t:
            sLetters[c] = sLetters.get(c,0) +1
        
        for c in s:
            if c not in sLetters:
               return c

            sLetters[c] -=1

            if sLetters[c] <=0:
                del sLetters[c]
        
        return list(sLetters)[0]