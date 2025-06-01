
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
# https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation