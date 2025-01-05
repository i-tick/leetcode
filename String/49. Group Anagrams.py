class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {}
        # temp = {}
        # for s in strs:
        #     for i in s:
        #         temp[i] = 1 + temp.get(i,0)
        #     res[temp].append(s) # temp is dict and it cant be used as key in another dict therefore diff approach
        # print(res)
        

        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord('z')-ord(i)] += 1
            res[tuple(count)].append(s) # count is list and cant be used as key in dict, therefore we change to tuple
        return list(res.values())
        