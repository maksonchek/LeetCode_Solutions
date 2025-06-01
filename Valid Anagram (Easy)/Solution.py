class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for w in s:
            s_dict[w] = s_dict.get(w,0) + 1
        for w in t:
            if w not in s_dict:
                return False
            else:
                t_dict[w] = t_dict.get(w,0) + 1
            if t_dict[w] > s_dict[w]:
                return False
        return True
        
