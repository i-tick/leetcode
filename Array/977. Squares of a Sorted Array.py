class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        l = 0
        r = len(nums)-1

        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                arr.append(nums[l]**2) 
                l+=1
            else:
                arr.append(nums[r]**2)
                r-=1                
        return arr[::-1]
                  
        
        
        
        
        
        
        # arr = []
        # for i in nums:
        #     arr.append(abs(i))
        # arr.sort()
        # for i in range(len(arr)):
        #     arr[i] = arr[i]**2

        # return arr
        