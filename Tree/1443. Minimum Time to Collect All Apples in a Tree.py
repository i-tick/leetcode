
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            

        def dfs(cur, parent):
            time = 0
            
            if len(adj[cur])==0:
                return 0

            for child in adj[cur]:
                if child == parent:
                    continue
                childTime = dfs(child, cur)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            return time

        return dfs(0, -1)
        