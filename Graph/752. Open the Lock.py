class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        def children(code):
            res = []
            for i in range(len(code)):
                plus1 = str((int(code[i])+1)%10)
                minus1 = str((int(code[i])-1)%10)

                pluscode = code[:i]+plus1+code[i+1:]
                minuscode = code[:i]+minus1+code[i+1:]
                res.append(pluscode)
                res.append(minuscode)
            return res
        
        vis = set(deadends)
        def bfs(q):
            while q:
                for _ in range(len(q)):
                    code,turns = q.popleft()
                    if code==target:
                        return turns

                    for child in children(code):
                        if child not in vis:
                            vis.add(child)
                            q.append((child,turns+1))
                        
            return -1


        q = deque()
        q.append(('0000',0))
        return bfs(q)
        