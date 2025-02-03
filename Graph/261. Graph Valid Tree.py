class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check for cycle
        if len(edges)>(n-1) or len(edges)<(n-1):
            return False
        
        # build neighbour list
        neigh = {i:[] for i in range(n)}
        for i,j in edges:
            neigh[i].append(j)
            neigh[j].append(i)


        #check if all nodes are connected
        vis = set()
        def dfs(n,par):
            if n in vis:
                return
            vis.add(n)
            for i in neigh[n]:
                if i==par:
                    continue
                dfs(i,n)
        dfs(0,-1)
        return len(vis)==n