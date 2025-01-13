class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        res = ""
        if l1>=l2:
            for i in range(l2):
                res += word1[i]+word2[i]
            res+=word1[l2:l1]
        else:
            for i in range(l1):
                res += word1[i]+word2[i]
            res+=word2[l1:l2]
        return res