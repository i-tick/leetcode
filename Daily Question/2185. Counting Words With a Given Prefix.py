class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        c = 0
        for i in words:
            if i[:l]==pref:
                c+=1
        return c
        