class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        h1 = {}
        h2 = {}
        res = 0
        res_array = []
        vis = set()
        for i in range(len(A)):
            h1[A[i]] = 1+h1[A[i]] if A[i] in h1 else 1
            h2[B[i]] = 1+h2[B[i]] if B[i] in h2 else 1
            if A[i] in h2 and A[i] not in vis:
                vis.add(A[i])
                res+=1
            if B[i] in h1 and B[i] not in vis:
                vis.add(B[i])
                res+=1
            res_array.append(res)
        return res_array