# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         map_array = defaultdict(list)
#         nodes = set()
#         i = 0
#         for x,y in equations:
#             nodes.add(x)
#             nodes.add(y)
#             map_array[x].append([y,values[i]])
#             map_array[y].append([x,1/values[i]])
#             i+=1

#         def bfs(src,tar):
#             nonlocal vis
#             q = deque()
#             if src not in nodes or tar not in nodes:
#                 return -1
#             q.append([src,1])
#             res = 1
#             vis.add(src)

#             while q:
#                 for _ in range(len(q)):
#                     x,val = q.popleft()
#                     if x==tar:
#                         return val

#                     for y,value in map_array[x]:
#                         if y in vis:
#                             continue
#                         vis.add(y)
#                         q.append([y,val*value])
#             return -1
               
#         res = []
#         for x,y in queries:
#             if x in nodes and y in nodes:
#                 vis = set()
#                 val = bfs(x,y)
#                 res.append(val)
#             else:
#                 res.append(-1)
#         return res






from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        var = set()
        for eq in equations:
            for x in eq:
                var.add(x)
            n = len(var)
        ind_map = {x:ind for ind,x in enumerate(list(var))}

        par = [(i,1.0) for i in range(n)]
        rank = [1 for i in range(n)]

        def find(ind):
            if type(ind) is str:
                ind = ind_map[ind]

            if par[ind][0]!=ind:
                par_ind, mup = find(par[ind][0])
                par[ind] = (par_ind, mup * par[ind][1])
            return par[ind]

        def union(a,b,x):
            ind_a, ind_b = ind_map[a], ind_map[b]
            par_a, mup_a = find(a)
            par_b, mup_b = find(b)

            if rank[par_a] > rank[par_b]:
                par_a, mup_a, par_b, mup_b = par_b, mup_b, par_a, mup_a
                x = 1.0 / x
            rank[par_b] = rank[par_a] + rank[par_b]
            par[par_a] = (par_b, (mup_b*x)/mup_a)

        for i, (j, k) in enumerate(equations):
            union(j, k, values[i])

        res = []

        for query in queries:
            if query[0] not in ind_map or query[1] not in ind_map:
                res.append(-1.0)
                continue
            a, b = find(query[0]), find(query[1])
            if a[0] != b[0]:
                res.append(-1.0)
            else:
                res.append(a[1] / b[1])
        
        return res




        