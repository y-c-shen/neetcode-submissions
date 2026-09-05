class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                new_node = Node()
                curr.children[c] = new_node
                curr = new_node
        curr.end = True

    
    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                elif c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
            return curr.end
        return dfs(0, self.root)

                


            
        
