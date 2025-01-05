class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        maparray = {i:[] for i in range(numCourses)}
        for cur,pre in prerequisites:
            maparray[cur].append(pre)

        res = []
        visited = set()
        stack = set()
        def dfs(cur):
            if cur in visited: return False
            if cur in stack: return True

            visited.add(cur)
            
            for i in maparray[cur]:
                if not dfs(i): return False
            res.append(cur)
            stack.add(cur)
            visited.remove(cur)
            return True


        for cur in range(numCourses):
            if not dfs(cur):
                return []

        return res
        