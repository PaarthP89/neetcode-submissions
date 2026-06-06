class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = defaultdict(int)
        for letter in s:
            first_word[ord(letter)] += 1
        second_word = defaultdict(int)
        for letter in t:
            second_word[ord(letter)] += 1
        return first_word == second_word