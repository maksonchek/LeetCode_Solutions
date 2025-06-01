#Класс defaultdict() модуля collections ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда вызывается функция, 
#которая возвращает значение по умолчанию для новых значений. Другими словами Класс defaultdict() представляет собой словарь со значениями по умолчанию.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            sword = ''.join(sorted(word))
            anagram[sword].append(word)
        return list(anagram.values())