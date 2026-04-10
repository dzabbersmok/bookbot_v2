import sys
from stats import word_count, char_counter, char_sort

def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()

def main():
    # book_path = 'books/frankenstein.txt'

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = word_count(text)
        char_count = char_counter(text)
        char_sorted = char_sort(char_count)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in char_sorted:
            if not char["char"].isalpha():
                continue

            print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")

main()