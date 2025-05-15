import sys
from stats import count_words, get_book_text, count_chars, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    char_counts = count_chars(book_text)

    sorted_chars = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()