class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = []
        for inter in intervals:
            if len(ans) == 0:
                ans.append(inter)
            else:
                if ans[-1][1] >= inter[0]:
                    if ans[-1][1] < inter[1]:
                        ans[-1][1] = inter[1]
                    # if ans[-1][0] > inter[0]:
                    #     ans[-1][0] = inter[0]
                elif ans[-1][1] < inter[0]:
                    ans.append(inter)
        return ans