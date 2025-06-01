class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        if digits[n] == 9:
            if n+1==1:
                digits.append(0)
                digits[n] = 1
            else:
                digits[n] = 0 
                for i in range(1, n+1):
                    if digits[n-i] == 9 and n-i == 0:
                        digits[0] = 1
                        digits.append(0)
                    elif digits[n-i] == 9 and n-i != 0:
                        digits[n-i] = 0
                    elif digits[n-i] != 9:
                        digits[n-i] += 1
                        break
        else:
            digits[n] += 1
        return digits