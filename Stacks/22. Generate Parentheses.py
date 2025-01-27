class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        ress = ''
        def backtracking(openN, closeN):
            nonlocal ress
            if openN == closeN == n:
                res.append(ress)
            if openN>closeN:
                if openN<n:
                    ress+='('
                    backtracking(openN+1,closeN)
                    ress = ress[:-1]
                if closeN<n:
                    ress+=')'
                    backtracking(openN,closeN+1)
                    ress = ress[:-1]
            else:
                if openN<n:
                    ress+='('
                    backtracking(openN+1,closeN)
                    ress = ress[:-1]
                    
        backtracking(0,0)
        return res