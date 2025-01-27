class Solution:
    def decodeString(self, s: str) -> str:
        c = []
        a = []

        k = 0
        r = ''

        for i in s:
            if i.isdigit():
                k = (k*10)+int(i)
            elif i == '[':
                a.append(r)
                c.append(k)
                r = ''
                k=0
            elif i==']':
                print(r)
                temp = r
                r = a.pop()
                count = c.pop()
                r += temp * count
            else:
                r+=i
        return r