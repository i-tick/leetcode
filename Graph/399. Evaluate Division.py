class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map_array = defaultdict(list)
        nodes = set()
        i = 0
        for x,y in equations:
            nodes.add(x)
            nodes.add(y)
            map_array[x].append([y,values[i]])
            map_array[y].append([x,1/values[i]])
            i+=1

        def bfs(src,tar):
            nonlocal vis
            q = deque()
            if src not in nodes or tar not in nodes:
                return -1
            q.append([src,1])
            res = 1
            vis.add(src)

            while q:
                for _ in range(len(q)):
                    x,val = q.popleft()
                    if x==tar:
                        return val

                    for y,value in map_array[x]:
                        if y in vis:
                            continue
                        vis.add(y)
                        q.append([y,val*value])
            return -1
               
        res = []
        for x,y in queries:
            if x in nodes and y in nodes:
                vis = set()
                val = bfs(x,y)
                res.append(val)
            else:
                res.append(-1)
        return res