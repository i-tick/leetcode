from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        avail_sup = set(supplies)
        
        # Initialize indegree for all recipes and supplies
        q = deque()
        for sup in supplies:
            indeg[sup] = 0
            q.append(sup)
        for i, rec in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in avail_sup:
                    indeg[rec]+=1
                    graph[ing].append(rec)
            if indeg[rec] == 0:
                q.append(rec)
                indeg[rec] = 0
        res = []
        # Perform topological sort using Kahn's algorithm
        while q:
            node = q.popleft()
            if node in recipes:
                res.append(node)

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return res
        
        