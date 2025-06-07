from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of characters to their order index
        # This will help us compare characters based on the alien dictionary order
        order_index = {}
        for i in range(len(order)):
            order_index[order[i]] = i

        # Compare adjacent words in the list
        # If any pair of adjacent words is not in the correct order, return False
        # We compare characters of the two words until we find a difference
        # If the first word's character comes after the second word's character in the alien order, return False
        # If we reach the end of the first word and the second word is longer, it's still valid
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                # If we reach the end of the first word, it means it's a prefix of the second word
                if j == len(w2):
                    return False
                # If characters at position j are different, we compare their order
                if w1[j]!=w2[j]:
                    # If the character in the first word comes after the character in the second word in the alien order, return False
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True
    # end of class Solution
    # time complexity: O(n * m), where n is the number of words and m is the average length of the words
    # space complexity: O(1), since the order mapping is of fixed size (26 characters)

        