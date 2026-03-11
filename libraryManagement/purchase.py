import colors
def purchase_books():
    print(f"{colors.GREEN}----Purchase  books---{colors.RESET}")
    try:
        with open("Available_Books.txt", 'r',encoding='utf-8') as file:
            books = file.readlines()            
            
            all_lines= [line.strip() for line in (books) if line.strip()]
            
            if not all_lines:
                print('Something went wrong')
                return
            
            header = all_lines[0]
            book_entries = all_lines[1:]
            if not  book_entries:
                print('Sorry, No Books available to purchase.')
                return
            
            print(f'{colors.BLUE}{header}{colors.RESET}')
            for idx, books in enumerate(book_entries,start=1):
                print(f'{colors.YELLOW}{idx}:{colors.RESET} {books}')
            
            
    except Exception as e:
        print(e)
if __name__ ==" __main__":
    purchase_books()