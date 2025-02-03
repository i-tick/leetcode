class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank  = [1]*(len(edges)+1)
        par = [i for i in range(len(edges)+1)]

        def find(n):
            p = par[n]

            if p!=n:
                return find(p)
            return p

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False
            par[max(p1,p2)]=min(p1,p2)

            return True

        res = set()
        for i,j in edges:
            if not union(i,j):
                return [i,j]
