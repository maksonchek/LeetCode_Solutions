class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        types = {
            "(": [")",True],
            "{": ["}",True],
            "[": ["}",True],
            ")": ["(",False],
            "}": ["{",False],
            "]": ["[",False],                             
        }
        for st in s:
            if types[st][1] == True:
                stack.append(st)
            elif types[st][1] == False:
                if len(stack) == 0:
                    return False
                else:
                    p = stack.pop()
                    if p != types[st][0]:
                        return False
        if len(stack) != 0:
            return False
        return True
    
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or pairs[stack.pop()] != i:
                return False
        return len(stack) == 0
