class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        edges = set()
        vis = set()
        neighbors = defaultdict(list)
        for a,b in connections:
            edges.add((a,b))
            neighbors[a].append(b)
            neighbors[b].append(a)

        q = deque()
        q.append(0)
        c = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                vis.add(x)

                for nei in neighbors[x]:
                    if nei in vis:
                        continue
                    if (x,nei) in edges:
                        c+=1
                    vis.add(nei)
                    q.append(nei)
        return c

        