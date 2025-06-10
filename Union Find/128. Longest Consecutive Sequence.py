from collections import Counter, defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in c.keys():
            if i-1 in c.keys():
                continue
            temp=1
            for j in range(1,len(nums)+1):
                if i+j in c.keys():
                    temp+=1
                else:
                    break
            res = max(res,temp)
        return res 
    # time O(n), space O(n)
    # The function iterates through the unique elements in the input list `nums`, checking for consecutive sequences starting from each element.
    # If an element `i` is the start of a sequence (i.e., `i-1` is not in the set), it counts how many consecutive elements follow it.
    # The maximum length of these sequences is tracked and returned as the result.
    # The use of `Counter` allows for efficient checking of the existence of elements in the list, making the solution efficient even for larger inputs.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_n = set(nums)
        par = {}
        for i in nums:
            if i+1 in set_n:
                par[i] = i+1
            else:
                par[i] = i
        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            return par[n]

        groups = defaultdict(set)
        len_max = 0
        for i in nums:
            new_par = find(i)
            groups[new_par].add(i)
            len_max = max(len_max, len(groups[new_par]))
        return len_max
    # time O(n), space O(n)
    # The function uses a union-find structure to group consecutive numbers together.
    # It initializes a parent mapping for each number, linking it to the next consecutive number if it exists.