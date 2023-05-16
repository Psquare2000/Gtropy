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
                return None
            node = node.children[char]
        if node.is_word:
            return word
        else:
            return self.find_closest_word(node, word)

    def find_closest_word(self, node, prefix):
        closest_word = prefix
        closest_distance = float('inf')

        for char, child_node in node.children.items():
            word = self.find_closest_word(child_node, prefix + char)
            if len(word) < closest_distance:
                closest_word = word
                closest_distance = len(word)

        return closest_word

# Creating an instance of the dictionary
my_dictionary = Dictionary()

# Predefined text file path
file_path = "DICT.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            my_dictionary.add_word(word)
    print("Dictionary created successfully!")

    # Searching for a word in the dictionary
    search_word = input("Enter a word to search in the dictionary: ")
    found_word = my_dictionary.search_word(search_word)

    if found_word:
        print(f"Word found in the dictionary: {found_word}")
    else:
        closest_word = my_dictionary.find_closest_word(my_dictionary.root, search_word)
        print(f"No matching word found. Closest word in the dictionary: {closest_word}")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
