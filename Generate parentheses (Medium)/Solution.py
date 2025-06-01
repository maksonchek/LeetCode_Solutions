class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cl = 0
        op = 0
        res = []
        stack = []

        def rec(cl, op):
            if cl == op == n:
                res.append("".join(stack))
            if op < n:
                stack.append('(')
                rec(cl, op+1)
                stack.pop()
            if cl < op:
                stack.append(')')
                rec(cl+1, op)
                stack.pop()
            return res
        return rec(cl, op)