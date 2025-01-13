class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = list(counter.keys())
        keys.sort()
        arr = []
        min_key = min(keys)
        max_key = max(keys)
        for i in range(min_key,max_key+1):
            if i not in counter:
                arr.append(0)
            else:
                arr.append(i*counter[i])
        print(arr)
        res = []
        if len(arr)<2:
            return arr[0]

        
        res.append(arr[0])
        res.append(max(arr[0],arr[1]))
        for i in range(2,len(arr)):
            res.append(max(res[i-1],res[i-2]+arr[i]))
        return res[-1]