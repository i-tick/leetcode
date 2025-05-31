from collections import defaultdict
from typing import List


class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # seen = set()
        # res = set()

        # for i in range(len(s)-9): # o(n-10+1)
        #     idx = s[i:i+10] # o(10)
        #     if idx in seen:
        #         res.add(idx) # o(1)
        #     seen.add(idx)
        # return list(res) 

        # # time complexity: o((n-9)*10) : o((n-k+1)k) worst k is const so o(n)
        # # space: o((n-k+1)k)



    def getVal(self, c):
        if c=='A': return 1
        if c=='C': return 2
        if c=='G': return 3
        return 4

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        h = 0
        w = 4
        sub = 4**9
        result = []
        i = 0
        hash = defaultdict()
        for c in s:
            i+=1
            h = h*w + self.getVal(c)
            if i>=10:
                print(h)
                hash[h]+=1
                if hash[h]==2:
                    result.append(s[i-10:i])
                h -= sub*self.getVal(s[i-10])
        return result
        # time complexity: o(n)
        # space complexity: o(n) for the hash map
