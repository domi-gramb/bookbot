def get_book_text(filepath):
    # Open the file using a with block
    with open(filepath) as f:
        # Read the file contents
        file_contents = f.read()
    # Return the contents
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    # Create an empty dictionary to store character counts
    char_counts = {}
    
    # Loop through each character in the text
    for char in text:
        # Convert character to lowercase
        char = char.lower()
        
        # Add or update the count for this character
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Return the completed dictionary
    return char_counts

def sort_char_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        chars_list.append(char_info)
    
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list