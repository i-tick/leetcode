class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n):
            if n in visit:
                return

            visit.add(n)
            for i in adj[n]:
                dfs(i)
        c = 0
        for i in range(n):
            if i not in visit:
                c+=1
                dfs(i)
        return c

        