

class Trie:

    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node:
                curr_node[w] = {}
            curr_node = curr_node[w]
        curr_node["*"] = "*"

    def check_if_word_exist(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node:
                return False
            curr_node = curr_node[w]

        return 'Full' if "*" in curr_node else "Partial"


class TrieV2:

    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.children = {}  # [None]*26
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode("*")

    def add_word(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = self.TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def check_if_word_exist(self, word):
        if word == "": return True
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return "Full" if curr_node.is_end else "Partial"


class TrieV21:

    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.children = {}  # [None]*26
            self.is_end = 0

    def __init__(self):
        self.root = self.TrieNode("*")

    def add_word(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = self.TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.is_end += 1

    def check_if_word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.is_end


class TrieV3:

    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.children = [None] * 26
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode("*")

    @staticmethod
    def char_to_idx(char):
        return ord(char) - ord('a')

    def add_word(self, word):
        curr_node = self.root
        for char in word:
            if not curr_node.children[self.char_to_idx(char)]:
                curr_node.children[self.char_to_idx(char)] = self.TrieNode(char)
            curr_node = curr_node.children[self.char_to_idx(char)]
        curr_node.is_end = True

    def check_if_word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for char in word:
            if not curr_node.children[self.char_to_idx(char)]:
                return False
            curr_node = curr_node.children[self.char_to_idx(char)]

        return "Full" if curr_node.is_end else "Partial"


if __name__ == '__main__':
    tries = [Trie(), TrieV2(), TrieV3(), TrieV21()]
    words = ['wait', 'waiter', 'shop', 'shopper', 'shop']
    for w in words:
        for trie in tries:
            trie.add_word(w)

    for trie in tries:
        print(f"USING Trie: \t {trie.__class__.__name__} ==> ")
        print(f'{"wait"} {trie.check_if_word_exist("wait")}')
        print(f'{"waite"} {trie.check_if_word_exist("waite")}')
        print(f'{"shop"} {trie.check_if_word_exist("shop")}')
        print(f'{"shope"} {trie.check_if_word_exist("shope")}')
        print(f'{"shopp"} {trie.check_if_word_exist("shopp")}')