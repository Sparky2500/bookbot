def get_book_text(file_path):
    book=""
    with open(file_path) as f:
        book = f.read()
    return book

def main():
    words=[]
    whole_book = get_book_text("books/frankenstein.txt")
    words = whole_book.split()
    num_word=len(words)
    print(f"{num_word} words found in the document")

main()