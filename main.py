from stats import num_words, character_total, sorted_list


def get_book_text(frankenstein):
    with open(frankenstein) as f:
        file_contents = f.read()
    return file_contents


def main():
    entire_text = get_book_text("./books/frankenstein.txt")
    print(f'''================== BOOKBOT ==================
Analyzing book found at books/frnkenstein.txt...
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


