class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst = {}
        mapts = {}

        if len(s) == len(t):
            for i in range(len(s)):
                c1 = s[i]
                c2 = t[i]

                if ((c1 in mapst and mapst[c1]!=c2) or (c2 in mapts and mapts[c2]!=c1)):
                    return False

                mapst[c1]=c2
                mapts[c2]=c1
                
            return True
        return False
        