class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0]*len(code)
        if k>0:
            
            for i in range(1,len(code)+1):
                idx = i-1
                i_start = (idx+1) % len(code) if idx+1 > len(code) else idx+1
                i_end = (idx+1+k) % len(code) if (idx+1+k) >len(code) else (idx+1+k)
                print(i_start,i_end)
                if i_end < i_start:
                    res[idx] = sum(code[i_start:]) + sum(code[:i_end])
                else:
                    res[idx] = sum(code[i_start:i_end])

        if k<0:
            
            for i in range(0,len(code)):
                idx = i
                i_start = (idx) % len(code) if idx < 0 else idx
                i_end = (idx+k) % len(code) if (idx+k) < 0 else (idx+k)
                print(i_start,i_end)
                if i_start < i_end:
                    res[idx] = sum(code[i_end:]) + sum(code[:i_start])
                else:
                    res[idx] = sum(code[i_end:i_start])

        return res
        