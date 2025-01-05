class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and (i+1,j+1) not in edges and (j+1,i+1) not in edges and isConnected[i][j]:
                    edges.add((i+1,j+1))
        edges = list(edges)
        n = len(isConnected)
        
        rank = [1]*(n+1)
        par = [i for i in range(n+1)]
        

        def find(n):
            p = par[n]

            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1==p2:
                return 0

            if rank[p1]>=rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1

        res = n

        for i,j in edges:
            res -= union(i,j)
        print(par)
        return res

            

        