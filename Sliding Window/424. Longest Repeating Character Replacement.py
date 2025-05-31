class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash = {}
        res = 0
        l = 0
        max_freq = float("-inf")
        for r in range(len(s)):
            if s[r] in hash:
                hash[s[r]] +=1
            else:
                hash[s[r]] = 1
            max_freq = max(max_freq, hash[s[r]])

            while (r-l+1) - max_freq>k:
                hash[s[l]]-=1
                l+=1
            res = max(res, r-l+1)

        return res
        # Time complexity: O(n)
        # Space complexity: O(1) since the hash map will have at most 26 characters
        # Explanation: We maintain a sliding window [l, r] and a hash map to count the frequency of characters.
        # When the number of characters that need to be replaced exceeds k, we shrink the window from the left.
        # The maximum length of the window is updated at each step.