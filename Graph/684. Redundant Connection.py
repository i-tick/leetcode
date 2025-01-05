class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank  = [1]*(len(edges)+1)
        par = [i for i in range(len(edges)+1)]

        def find(n):
            p = par[n]

            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False

            if rank[n1]>=rank[n2]:
                par[p2]=p1
                rank[n1]+=rank[n2]
            else:
                par[p1]=p2
                rank[2]+=rank[n1]

            return True

        res = set()
        for i,j in edges:
            if not union(i,j):
                return [i,j]
