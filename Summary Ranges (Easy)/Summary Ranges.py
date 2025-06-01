class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s = 0
        ans = []
        e=0
        for i in range(len(nums)): #Ошибка была тут. Обращать внимание на момент, что он начинает с 0! 0 1 2 3 4 5 кфтпу = 6
            if i+1 <= len(nums) -1:
                if nums[i]+1 == nums[i+1]:
                    e = i+1
                else:
                    if e != s:
                        ans.append(f"{nums[s]}->{nums[e]}")
                    else:
                        ans.append(f"{nums[e]}") 
                    s = i + 1
                    e = i + 1
            else:
                if e != s:
                    ans.append(f"{nums[s]}->{nums[e]}")
                else:
                    ans.append(f"{nums[e]}") 
            
        return ans      
