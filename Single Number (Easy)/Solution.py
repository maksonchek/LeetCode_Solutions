# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0
#         for num in nums:
#             ans ^= num #Это исключающее или!!!
#         return ans
    
def singleNumber( nums):
        ans = 0
        for num in nums:
            ans ^= num #Это исключающее или!!!
        return ans
#В силу коммутатикности XOR это работет
# https://habr.com/ru/companies/vdsina/articles/538298/
mas = [1,4,7,3,1,7,3,5,4,8,8]

print(singleNumber(mas))