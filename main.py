from stats import count_words
from stats import count_chars

def main():
    file_path = "books/frankenstein.txt"
    file_content = get_book_text(file_path)
    counted_words = count_words(file_content)
    print(f"Found {counted_words} total words")
    char_dict = count_chars(file_content)
    print (char_dict)


def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents


main()