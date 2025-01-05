class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = {i:[] for i in range(len(points))}
        n = len(points)

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        res = 0
        vis = set()
        minH = [[0,0]]
        while len(vis)!=n:
            cost,i = heappop(minH)

            if i in vis:
                continue
            # print(cost,i)
            res+=cost
            vis.add(i)
            for neig in adj[i]:
                heappush(minH,[neig[0],neig[1]])
        return res

        