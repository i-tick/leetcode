class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i,len(isConnected[0])):
                if i!=j and isConnected[i][j]:
                    edges[i+1].append(j+1)
                    edges[j+1].append(i+1)
        print(edges)
        n = len(isConnected)
        vis = set()

        def dfs(cur,par):
            if cur in vis:
                return 

            vis.add(cur)
            for nei in edges[cur]:
                if nei==par:
                    continue
                dfs(nei,cur)
            return 
        c = 0 
        for i in range(1,n+1):
            if i not in vis:
                dfs(i,-1)
                c+=1
        return c

        
    