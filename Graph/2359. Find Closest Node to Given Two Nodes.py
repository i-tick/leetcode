class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = {i:[] for i in range(len(edges))}
        for i, nei in enumerate(edges):
            adj[i].append(nei)
        def bfs(node, distmap):
            q = deque()
            q.append((node,0))
            distmap[node] = 0
            while q:
                src,d = q.popleft()
                for nei in adj[src]:
                    if nei not in distmap and nei!=-1:
                        q.append((nei, d + 1))
                        distmap[nei] = d + 1


        dist1 = {}
        dist2 = {}
        bfs(node1,dist1)
        bfs(node2,dist2)
        res = -1
        resd = float('inf')
        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                dist = max(dist1[i], dist2[i])
                if dist < resd:
                    resd, res = dist, i

        return res