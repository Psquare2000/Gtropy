class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    suggested_words = []
    did_you_mean=""

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
            # return self.find_closest_words(node, word)

    def find_closest_words(self, node, prefix):

        def traverse(node, current_word):
            if node.is_word:
                suggested_words.append(current_word)

            for char, child_node in node.children.items():
                traverse(child_node, current_word + char)

        traverse(node, prefix)
        return suggested_words

    def print_suggested_words(self, suggested_words):
        print("Suggested words:")
        for word in suggested_words:
            print(word)

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
        # suggested_words = my_dictionary.search_word(search_word)
        my_dictionary.print_suggested_words(found_word)

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
