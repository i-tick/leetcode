class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(temp,max_right)

        return arr
        