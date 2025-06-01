class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dictionary = {}
        for word in strs:
            sword = str(sorted(word))
            if sword not in dictionary:
                dictionary[sword] = []
            dictionary[sword].append(word)
        for i in dictionary:
            ans.append(dictionary[i])
        return ans