class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { ")" : "(", "]":"[", "}":"{"}

        for i in s:
            if i in brackets:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                    stack.append(i)
        if stack:
            return False
        return True
        