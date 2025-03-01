import sys
from stats import get_num_words, get_num_char, sorted_dicts_report




def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    with open("books/mobydick.txt") as file:
        print(file.read(10))  # Reads and prints the first 10 characters


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(sys.argv[1]) + "...")
    print("----------- Word Count ----------")
    print("Found " + get_num_words(get_book_text(sys.argv[1])) + " total words")
    print("--------- Character Count -------")

    for char_dict in sorted_dicts_report(get_num_char(get_book_text(sys.argv[1]))):
        print( char_dict["char"] + ": " + str(char_dict["count"]) )

    print("============= END ===============")

main()