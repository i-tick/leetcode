class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        textc = Counter(text)

        res = float('inf')
        print(balloon)
        print(textc)
        for i in balloon:
            res = min(res,textc[i]//balloon[i])
        return res
        