class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for w in s:
            if w != "#":
                stack_s.append(w)
            else:
                if len(stack_s) != 0:
                    stack_s.pop()
        for w in t:
            if w != "#":
                stack_t.append(w)
            else:
                if len(stack_t) != 0:
                    stack_t.pop() 
        return stack_t == stack_s
