class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        c = 0
        boxes = list(boxes)
        pre_sum = 0
        for i in range(len(boxes)):
            if boxes[i]=='1':
                c+=1
                pre_sum += i

        vis = 0
        res = []
        for i in range(len(boxes)):
            res.append(pre_sum)
            if boxes[i]!='0':
                vis+=1
            pre_sum+=((-1)*(c-vis)) + (1*(vis))
        return res