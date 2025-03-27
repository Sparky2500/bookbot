import sys

def get_book_text(file_path):
    full=""
    with open(file_path) as f:
        full = f.read()
    return full

from stats import count_words
from stats import count_char
from stats import char_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    whole_book = get_book_text(path)
    num_word = count_words(whole_book)
    let_count = count_char(whole_book)
    sorted = char_sort(let_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for dict in sorted:
        print(str(dict["character"])+": "+str(dict["number"]))
    print("============= END ===============")

main()