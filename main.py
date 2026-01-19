def main():
    file_path = "books/frankenstein.txt"
    file_content = get_book_text(file_path)
    counted = count_words(file_content)
    print(f"Found {counted} total words")


def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents


def count_words(file_content):
    num_words = len(file_content.split())
    return num_words

main()