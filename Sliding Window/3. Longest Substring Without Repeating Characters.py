class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     res = 0
    #     l = 0
    #     charset = set()

    #     for r in range(len(s)):
    #         while s[r] in charset:
    #             charset.remove(s[l])
    #             l+=1
    #         charset.add(s[r])
    #         res = max(res,r-l+1)
    #     return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        # Time complexity: O(n)
        # Space complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.
        # Explanation: We maintain a sliding window [l, r] and a hash map to store the last index of each character.
        # When we encounter a character that is already in the current substring, we move the left pointer l to the right of the last occurrence of that character.
        # The maximum length of the substring without repeating characters is updated at each step.
#         # The algorithm uses a two-pointer technique to maintain the sliding window and a hash map to track the last index of each character.
#         # The final result is the length of the longest substring without repeating characters.
#         # If the string is empty, the result is 0.