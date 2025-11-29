from stats import num_words, character_total, sorted_list
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def check_arguments(argument):
    if len(argument) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    check_arguments(sys.argv)
    entire_text = get_book_text(sys.argv[1])
    print(f'''================== BOOKBOT ==================
Analyzing book found at {sys.argv[1]}...
----------------- Word Count ------------------
Found {num_words(entire_text)} total words
--------------- Character Count ---------------''')
    letters= character_total(entire_text)
    now_sort = sorted_list(letters)
    for dictionary in now_sort:
        if not dictionary["char"].isalpha():
            continue
        print(f"{dictionary["char"]}: {dictionary["num"]}")

    print("================== END ==================")
 
   #struggled on dictionary inside of list

main()


