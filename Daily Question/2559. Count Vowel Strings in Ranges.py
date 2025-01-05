class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum_array = [0]*(len(words)+1)
        vowels = ('a','e','i','o','u')
        c = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][len(words[i])-1] in vowels:
                c+=1
            prefix_sum_array[i+1] = c
        res = []
        for i,j in queries:
            res.append(prefix_sum_array[j+1]-prefix_sum_array[i])
        return res