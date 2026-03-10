import colors
def sell_books():
    print(f'{colors.GREEN}selling corner..{colors.RESET}')
    try:
        book_name = input("Enter the book name: ")
        book_name_check = book_name.strip()
    except Exception as e:
        print(e )
        return
    if not book_name_check:
        print('Book name cant be empty or only spaces \n')
    page_number = input("Enter the page number: ".strip())
    if not page_number:
        print('Page number cant be empty')
    try:
        page_numbers = int(page_number)
    except:
        print("Page number must be a integer number \n")
        return
    
    if page_numbers < 0: 
        print("Page number can't be negative!")
        
    try:
        with open ('Available_Books.txt','a+') as file:
            book_entry= f'{book_name}-Page Number: {page_number} \n'
            for line in file:
                if line == book_name:
                    print("The book already exists.")
                    return
            file.write(book_entry)
            print(f"{book_name} added to the inventory")
    except Exception as e:
        print(e)
        return