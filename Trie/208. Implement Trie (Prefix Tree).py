class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child={}
        self.end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current= self.child
        for ch in word:
            if ch not in current:
                current[ch]={}
                current=current[ch]
            else:
                current=current[ch]
        current[self.end]=True 
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.child
        for ch in word:
            if ch not in current:
                return False
            
            else:
                current =current[ch]
     
        return self.end in current 
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.child
        for ch in prefix:
            if ch not in current:
                return False
            else:
                current=current[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
