class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = set()
        def dfs(i):
            nonlocal n
            if i in vis:
                return
            vis.add(i)
            n-=1
            for j in rooms[i]:
                dfs(j)

        dfs(0)
        return True if n==0 else False
