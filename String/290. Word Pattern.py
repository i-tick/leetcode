class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        
        charToWord = {}
        wordToChar = {}

        for i,n in enumerate(pattern):
            if pattern[i] in charToWord and charToWord[pattern[i]]!=s[i]:
                return False
            if s[i] in wordToChar and wordToChar[s[i]]!=pattern[i]:
                return False

            charToWord[pattern[i]] = s[i]
            wordToChar[s[i]] = pattern[i]
        return True