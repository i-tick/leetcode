class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(' ')
        l = [x for x in l if x!='']
        return len(l[-1])