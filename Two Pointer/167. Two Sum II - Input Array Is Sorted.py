class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0,len(numbers)-1

        while l<r:
            sumt = numbers[l]+numbers[r]

            if sumt>target:
                r-=1
            elif sumt<target:
                l+=1
            else:
                return [l+1,r+1]