class Solution:
    def reverseWords(self, s: str) -> str:
        word_mas = s.split(" ")
        for i, word in enumerate(word_mas):
            word_mas[i] = word_mas[i][::-1]
        return " ".join(word_mas)
                