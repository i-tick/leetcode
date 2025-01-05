class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        


        # this is m*n time complexity


        # shift_array = [0]*len(s)
        # for i in shifts:
        #     if i[2]==1:
        #         for j in range(i[0],i[1]+1):
        #             shift_array[j]+=1
        #     if i[2]==0:
        #         for j in range(i[0],i[1]+1):
        #             shift_array[j]-=1
        # result = ''
        # for i in range(len(s)):
        #     val = shift_array[i]
        #     res = (ord(s[i]) - ord('a') + val)%26
        #     result += chr(ord('a')+res)
        # return result
        



        # try to do with prefix sum - since not everything starts from 0, so keep start and end of prefix sum
        # i is start, j is end
        prefix_array = [0]*(len(s)+1)
        for i,j,dir in shifts:
            prefix_array[j+1]+=1 if dir==1 else -1
            prefix_array[i]+=-1 if dir==1 else 1

        dif = 0
        result = ''
        # print(prefix_array)
        for i in reversed(range(1,len(s)+1)):
            dif += prefix_array[i]
            res = (ord(s[i-1]) - ord('a') + dif)%26
            result += chr(ord('a')+res)
        return result[::-1]