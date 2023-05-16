class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

# Creating an instance of the dictionary
my_dictionary = Dictionary()

# Reading words from a text file
file_path = "DICT.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            my_dictionary.add_word(word)
    print("Dictionary created successfully!")

    # Searching for a word in the dictionary
    search_word = input("Enter a word to search in the dictionary: ")
    if my_dictionary.search_word(search_word):
        print("Word found in the dictionary!")
    else:
        print(f"Did you mean {search_word}")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
