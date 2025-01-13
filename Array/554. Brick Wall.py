class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        border = defaultdict(int)

        for r in wall:
            pre = 0
            for i in range(len(r)):
                if i==len(r)-1:
                    break
                pre+=r[i]
                border[pre]+=1
        if len(border)==0:
            return len(wall)

        
        v = max(list(border.values()))
        print(v)
        return len(wall)-v
        