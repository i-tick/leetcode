class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_counter = Counter(s)
        t_counter = Counter(t)

        for i in s_counter:
            if not (i in t_counter and s_counter[i] == t_counter[i]):
                return False

        for i in t_counter:
            if not (i in s_counter and t_counter[i] == s_counter[i]):
                return False
        return True