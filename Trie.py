#___________________________________________________________________________

# Date Log: 08/07/24
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Difficulty: Medium
# Qnumber = 208

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#___________________________________________________________________________

# Date Log: 08/08/24
# Link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/
# Difficulty: Easy
# Qnumber = 3042

class Solution:
    
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        AnsCounter = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    AnsCounter += 1
        return AnsCounter
    
#___________________________________________________________________________

# Date Log: 08/08/24
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# Difficulty: Medium
# Qnumber = 211

class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

#___________________________________________________________________________