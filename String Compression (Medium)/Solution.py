class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0

        while i <= len(chars):
            count = 0
            letter = chars[i]
            while i <= len(chars) and letter == chars[i]:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            
            if count > 1:
                for num in str(count):
                    chars[ans] = num
                    ans += 1
        
        return ans 