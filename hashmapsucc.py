class Dictionary:
    def __init__(self):
        self.hash_map = {}

    def add_word(self, word):
        self.hash_map[word] = True

    def search_word(self, word):
        if word in self.hash_map:
            return word
        else:
            return None

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
        print("Word not found in the dictionary.")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
