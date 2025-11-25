from stats import num_words, character_total


def get_book_text(frankenstein):
    with open(frankenstein) as f:
        file_contents = f.read()
    return file_contents


def main():
    entire_text = get_book_text("./books/frankenstein.txt")
    print(f"Found {num_words(entire_text)} total words")
    print(character_total(entire_text))
   

main()


