class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        vis = set()
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i])<len(words[j]):
                    if words[i] not in vis and words[i] in words[j]:
                        res.append(words[i])
                        vis.add(words[i])
                else:
                    if words[j] not in vis and words[j] in words[i]:
                        res.append(words[j])
                        vis.add(words[j])
        return res