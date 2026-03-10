import colors
def sell_books():
    print(f'{colors.GREEN}selling corner..{colors.RESET}')
    while True:
        try:
            book_name = input(f"{colors.YELLOW}Enter the book name: {colors.RESET}")
            book_name_check = book_name.strip()
        except Exception as e:
            print(e )
            continue
        if not book_name_check:
            print(f'{colors.RED}Book name cant be empty or only spaces {colors.RESET}\n')
            continue
    
        try:
            page_number = int(input(f"{colors.YELLOW}Enter the page number: {colors.RESET}".strip()))
            if page_number < 0: 
                print(f"{colors.RED}Page number can't be negative! {colors.RESET}")
                continue
        except:
            print(f"{colors.RED}Page number must be a integer number {colors.RESET}\n")
            continue
        
        
        try:
            price = int(input(f"{colors.PURPLE}Price (USD): {colors.RESET}"))
            if price <0:
                print(f"{colors.RED}Price cant be negative number ")
                continue
        except ValueError:
            print(f"price must be a integer number{colors.RESET}")
            continue
        
        book_exist = False
        try:
            with open ('Available_Books.txt','a+') as file:
                file.seek(0)
                book_check = [line.strip() for line in file.readlines()]
                for books in book_check:
                    exiting_book = books.split('~')[0].strip()
                    if exiting_book == book_name:
                        book_exist = True
                        break
                if book_exist:
                   print(f"{colors.YELLOW}The Book {book_name} already exists. Try another one {colors.RESET}")
                else:
                    book_entry= f'{book_name} ~ {page_number}page ~ Price: {price}USD \n'
                    file.write(book_entry)
                    print(f"{colors.GREEN}{book_name} added to the inventory {colors.RESET}")
                    break       
        except Exception as e:
            print(f'{colors.RED} {e}{colors.RESET}')
            continue