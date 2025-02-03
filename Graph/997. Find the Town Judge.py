class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for i,j in trust:
            outgoing[i]+=1
            incoming[j]+=1

        for i in range(1,n+1):
            if outgoing[i]== 0 and incoming[i]==n-1:
                return i
        return -1