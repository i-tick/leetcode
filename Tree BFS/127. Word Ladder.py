import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Create a key by replacing one character with '*'
                key = word[:i] + "*" + word[i+1:]
                nei[key].append(word)

        queue = collections.deque([(beginWord, 1)])  # (current word, current length)
        visited = set([beginWord])

        while queue:
            current_word, length = queue.popleft()
            if current_word == endWord:
                return length
            # For each character in the current word, generate all possible transformations
            # by replacing one character with '*'
            # and check the neighbors in the dictionary
            for i in range(len(current_word)):
                key = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in nei[key]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
        return 0  # If we exhaust the queue without finding endWord, return 0