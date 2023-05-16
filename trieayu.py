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
        closest_word = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            closest_word += char
        else:
            if node.is_word:
                return closest_word

        return self.find_closest_word(node, closest_word)

    def find_closest_word(self, node, prefix):
        if node.is_word:
            return prefix

        closest_word = None
        for char, child_node in node.children.items():
            word = self.find_closest_word(child_node, prefix + char)
            if closest_word is None or len(word) < len(closest_word):
                closest_word = word
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
        closest_word = my_dictionary.search_word(search_word)
        print(f"No matching word found. Closest word in the dictionary: {closest_word}")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

