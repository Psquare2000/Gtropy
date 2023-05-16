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

        return self.find_closest_word(node, closest_word, word)

    def find_closest_word(self, node, prefix, target_word):
        closest_word = None
        closest_distance = float('inf')

        if node.is_word:
            distance = self.calculate_distance(prefix, target_word)
            if distance < closest_distance:
                closest_word = prefix
                closest_distance = distance

        for char, child_node in node.children.items():
            word = self.find_closest_word(child_node, prefix + char, target_word)
            distance = self.calculate_distance(word, target_word)
            if distance < closest_distance:
                closest_word = word
                closest_distance = distance

        return closest_word

    def calculate_distance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # deletion
                        dp[i][j - 1] + 1,  # insertion
                        dp[i - 1][j - 1] + 1  # substitution
                    )

        return dp[m][n]

# Creating an instance of the dictionary
my_dictionary = Dictionary()

# text file path
file_path = "DICT.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            my_dictionary.add_word(word)
    print("Dictionary created successfully!")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Searching for a word in the dictionary
search_word = input("Enter a word to search in the dictionary: ")
if search_word == "":
    print("please enter a word")
        
found_word = my_dictionary.search_word(search_word)

if found_word is search_word:
    print(f"Word found in the dictionary: {found_word}")
else:
    # closest_word = my_dictionary.search_word(search_word)
    # closest_word = found_word
    print(f"No matching word found. Did you mean {found_word} ?")