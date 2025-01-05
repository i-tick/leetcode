class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
        
class WordDictionary:

    def __init__(self):
        self.root= TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True
        

    def search(self, word: str) -> bool:
        cur = self.root


        def backtrack(i,root):
            cur = root

            for j in range(i,len(word)):
                c = word[j]

                if c == '.':
                    for child in cur.children.values():
                        if backtrack(j+1,child):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endofword
        return backtrack(0, self.root)
            

        return cur.endofword
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)