class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2!=0:
            return False
        c = 0
        w = 0
        for i in range(len(s)):
            if locked[i]=='0':
                w+=1
                continue
            if s[i]==')':
                c-=1
            else:
                c+=1

            if c<0:
                if w>0:
                    c+=1
                    w-=1
                else:
                    return False

        c = 0
        w = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i]=='0':
                w+=1
                continue
            if s[i]=='(':
                c-=1
            else:
                c+=1

            if c<0:
                if w>0:
                    c+=1
                    w-=1
                else:
                    return False

        return True