class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1,1]]
        if numRows < 3:
            return dp[:numRows]
        for _ in range(numRows-2):
            an = [1]
            for i in range(1,(len(dp[-1]))):
                an.append(dp[-1][i] + dp[-1][i-1])
            an.append(1)
            dp.append(an)
        return dp