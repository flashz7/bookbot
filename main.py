# Write a main function that uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
from stats import get_num_words, get_num_chars, sort_dict
import sys

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text
    
def main():
    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    dict_list = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["count"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()