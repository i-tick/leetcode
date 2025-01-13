class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(word1, word2):
            l1 = len(word1)
            l2 = len(word2)
            if l2<l1:
                return False
            
            if word1 == word2[:l1] and word1 == word2[l2-l1:]:
                return True
            return False


        c = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    c+=1
        return c
        