def get_book_text(frankenstein):
    with open(frankenstein) as f:
        file_contents = f.read()
    return file_contents



def main():
    print(get_book_text("./books/frankenstein.txt"))
    
    

main()

