class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        res = 0
        for i in tokens:
            if i in ['+','-','/','*']:
                x = num.pop()
                y = num.pop()
                if i == '+':
                    res = y+x
                if i == '-':
                    res = y-x
                if i == '*':
                    res = y*x
                if i == '/':
                    res = y/x
                    res = int(res)
                # print(res)
                num.append(res)
            else:
                num.append(int(i))
        return num[0]
        