import colors
def purchase_books():
    print(f"{colors.GREEN}----Purchase  books---{colors.RESET}")
    try:
        with open("Available_Books.txt", 'r+') as file:
            books = file.readlines()
            print("Book name ~ Page ~ Price (USD)")
            for index, book in enumerate(books):
                print(f'{index+1} {book[index+1].strip()}')
    except Exception as e:
        print(e)