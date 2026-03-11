import colors
def purchase_books():
    print(f"{colors.GREEN}----Purchase  books---{colors.RESET}")
    try:
        with open("Available_Books.txt", 'r+') as file:
            books = file.readlines()
            books_filterd = books[1:]
            print("Book name ~ Page ~ Price (USD)")
            for index, book in enumerate(books_filterd,start=1):
                print(f'{colors.YELLOW} {index}:{colors.RESET} {book.strip()}')
            choose_book = int(input('Enter he name/index of the book you want to buy: '))
            book_choosed = books_filterd[choose_book]
            print(f'{colors.PURPLE}You choose to buy {book_choosed} {colors.RESET}')
    except Exception as e:
        print(e)
if __name__ ==" __main__":
    purchase_books()