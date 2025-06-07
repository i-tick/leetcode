# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.



from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj_list = defaultdict(set)
        indeg = {}
        for word in words:
            for c in word:
                indeg[c] = 0

        
        # Build the adjacency list and calculate in-degrees
        # Compare adjacent words to determine the order of characters
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # if w2 is prefix of w1 & w1 is longer than w2, then return ""
            if len(w1)> len(w2) and w2 == w1[:min_len]:
                return ""
        
            # Compare characters until they differ
            # and build the adjacency list
            # If characters differ, add an edge from w1[j] to w2[j]
            # and increment the in-degree of w2[j]
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        indeg[w2[j]]+=1
                    break
        
        # Initialize the queue with nodes that have no incoming edges
        q = deque()
        for key in indeg:
            if indeg[key]==0:
                q.append(key)

        # Perform topological sort using Kahn's algorithm
        # Process nodes with no incoming edges and reduce in-degrees of their neighbors
        # If a neighbor's in-degree becomes zero, add it to the queue
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj_list[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        # If we can process all characters, we have a valid order
        # If not, return an empty string indicating a cycle or that not all characters can be processed
        if len(res) == len(indeg):
            return "".join(res)
        return ""
    
    # end of class Solution
    # time complexity: O(V + E)
    # space complexity: O(V + E)