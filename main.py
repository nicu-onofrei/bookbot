from stats import count_words
from stats import count_character
from stats import sorting_dictionaries
from stats import clean_print
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents


def main():
    #print (f"{get_book_text("books/frankenstein.txt")}")
    #count_words(get_book_text("books/frankenstein.txt"))
    #print(f"{count_character("books/frankenstein.txt")}")
    #print(get_book_text("books/frankenstein.txt"))
    #print(count_character(get_book_text("books/frankenstein.txt")))
    #sorting_dictionaries(count_character(get_book_text("books/frankenstein.txt")))
    #path = "books/frankenstein.txt"
    #print (f"Lungime parametrilor este {len(sys.argv)}")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count_words(get_book_text(path))
    print("--------- Character Count -------")
    clean_print(sorting_dictionaries(count_character(get_book_text(path))))
    print("============= END ===============")
main()
