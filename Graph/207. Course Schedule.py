class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maparray = {i:[] for i in range(numCourses)}
        for cur,pre in prerequisites:
            maparray[cur].append(pre)

        # print(maparray[0]== False)
        visited = set()

        # cycle detection
        def dfs(cur):
            if cur in visited: return False

            if len(maparray[cur])==0: return True
            
            visited.add(cur)
            for i in maparray[cur]:
                if not dfs(i): return False
            visited.remove(cur)
            maparray[cur] = []

            return True

        for cur in range(numCourses):
            if not dfs(cur):
                return False

        return True