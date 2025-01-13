class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i==0:
                prev = [1]
                res.append(prev)
            else:
                cur = [1]
                j = 1
                while (j<i):
                    cur.append(prev[j-1]+prev[j])
                    j+=1
                cur.append(1)

                res.append(cur)
                prev = cur
        return res