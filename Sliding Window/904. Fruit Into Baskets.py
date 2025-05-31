from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        res = 0
        l = 0
        c = 0

        for r in range(len(fruits)):
            if fruits[r] in freq:
                freq[fruits[r]] += 1
            else:
                freq[fruits[r]] = 1

            while len(freq)>2:
                freq[fruits[l]] -= 1

                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l+=1
            res = max(res, r-l+1)
        return res

            
        