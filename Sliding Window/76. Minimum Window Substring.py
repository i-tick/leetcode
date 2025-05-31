
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_t = Counter(t)
        need = sum(c_t.values())
        have = 0
        if len(s)==len(t):
            c_s = Counter(s)
            return s if c_s==c_t else ''
        if len(s)<len(t):
            return ''
        c_s = defaultdict(int)
        r_final = 0
        l_final = 0

       
        l = 0
        r = 0
        res = float('inf')
        for r in range(len(s)):
            c = s[r]
            c_s[c]+=1

            if c in c_t and c_s[c] <= c_t[c]:
                have+=1

            if have==need:
                while l<=r and have==need:
                    if r-l+1<res:
                        r_final = r
                        l_final = l
                        res = r-l+1
                    new_c = s[l]
                    if new_c in c_t and c_t[new_c]==c_s[new_c]:
                        have-=1
                    c_s[new_c]-=1
                    l+=1
    
        return s[l_final:r_final+1] if res!=float('inf') else ''
        # Time complexity: O(n)
        # Space complexity: O(m) where m is the size of the character set in t
        # Explanation: We maintain a sliding window [l, r] and a hash map to count the frequency of characters in s.
        # When the number of characters that need to be matched equals the number of characters in t, we try to shrink the window from the left.
        # The minimum length of the window is updated at each step.
#         # If the window contains all characters of t, we check if it's the smallest found so far.
#         # If the window does not contain all characters of t, we expand the window from the right.
#         # The final result is the smallest window that contains all characters of t.
#         # If no such window exists, we return an empty string.
#         # The algorithm uses a two-pointer technique to maintain the sliding window and a hash map to count character frequencies.