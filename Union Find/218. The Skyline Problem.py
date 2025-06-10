from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        cor = set()
        for building in buildings:
            for x in building[:2]:
                cor.add(x)
        cor = sorted(list(cor))
        n = len(cor)
        hts = [0]*n
        ind_map = {x:idx for idx, x in enumerate(cor)}
        buildings.sort(key = lambda x:-x[2])
        skyline = []

        par = [i for i in range(n)]
        def find(i):
            if i!=par[i]:
                par[i] = find(par[i])
            return par[i]
        
        def union(i,j):
            p1 = find(i)
            p2 = find(j)

            if p1!=p2:
                par[min(p1,p2)] = max(p1,p2)
        
        for left_x, right_x, height in buildings:
            left, right = ind_map[left_x], ind_map[right_x]
            
            while left < right: 
                left = find(left)

                if left < right:
                    union(left, right)
                    hts[left] = height
                    left += 1
        
        for i in range(n):
            if i == 0 or hts[i] != hts[i - 1]:
                skyline.append([cor[i], hts[i]])
        
        return skyline
# Time Complexity: O(n log n) for sorting the buildings and processing the skyline.
# Space Complexity: O(n) for the height array and the parent array in the union-find structure.
# The algorithm efficiently computes the skyline by leveraging a union-find structure to manage heights at different x-coordinates.
# The skyline is built by iterating through the sorted buildings and updating heights based on the union-find structure.

# Dry run for input: [[2,9,10],[3,7,15],[5,12,12]]

# Step 1: Collect all unique x-coordinates
# buildings = [[2,9,10],[3,7,15],[5,12,12]]
# cor = {2, 3, 5, 7, 9, 12}
# cor (sorted) = [2, 3, 5, 7, 9, 12]
# n = 6

# Step 2: Map x-coordinates to indices
# ind_map = {2:0, 3:1, 5:2, 7:3, 9:4, 12:5}

# Step 3: Sort buildings by descending height
# buildings = [[3,7,15],[5,12,12],[2,9,10]]

# Step 4: Initialize hts = [0,0,0,0,0,0], par = [0,1,2,3,4,5]

# Process building [3,7,15]:
# left_x=3, right_x=7, height=15
# left=1, right=3
# while left < right:
#   left=find(1)=1
#   union(1,3): par[1]=3
#   hts[1]=15
#   left=2
#   left=find(2)=2
#   union(2,3): par[2]=3
#   hts[2]=15
#   left=3 (exit loop)

# hts=[0,15,15,0,0,0], par=[0,3,3,3,4,5]

# Process building [5,12,12]:
# left_x=5, right_x=12, height=12
# left=2, right=5
# while left < right:
#   left=find(2)=3 (par[2]=3)
#   left=3
#   union(3,5): par[3]=5
#   hts[3]=12
#   left=4
#   left=find(4)=4
#   union(4,5): par[4]=5
#   hts[4]=12
#   left=5 (exit loop)

# hts=[0,15,15,12,12,0], par=[0,3,3,5,5,5]

# Process building [2,9,10]:
# left_x=2, right_x=9, height=10
# left=0, right=4
# while left < right:
#   left=find(0)=0
#   union(0,4): par[0]=4
#   hts[0]=10
#   left=1
#   left=find(1)=3 (par[1]=3)
#   left=3
#   union(3,4): par[3]=4
#   hts[3]=10 (but already 12, so overwritten)
#   left=4
#   left=find(4)=4
#   left=4 (exit loop)

# hts=[10,15,15,10,12,0], par=[4,3,3,4,5,5]

# Step 5: Build skyline
# i=0: hts[0]=10 (prev=none) -> [2,10]
# i=1: hts[1]=15 (prev=10) -> [3,15]
# i=2: hts[2]=15 (prev=15) -> skip
# i=3: hts[3]=10 (prev=15) -> [7,10]
# i=4: hts[4]=12 (prev=10) -> [9,12]
# i=5: hts[5]=0 (prev=12) -> [12,0]

# Final skyline: [[2,10],[3,15],[7,10],[9,12],[12,0]]