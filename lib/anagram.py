# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, anagram_list):
        matches = []
        for candidate in anagram_list:
            if self.is_anagram(candidate):
                matches.append(candidate)
        return matches

    def is_anagram(self, candidate):
        return sorted(self.word) == sorted(candidate.lower()) and self.word != candidate.lower()