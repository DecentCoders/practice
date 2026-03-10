import colors
def sell_books():
    print(f'{colors.GREEN}selling corner..{colors.RESET}')
    try:
        book_name = input("Enter the book name: ")
    except Exception as e:
        print(e)
        return
    if not book_name:
        print('Book name cant be empty')
    page_number = input("Enter the page number: ")
    try:
        page_numbers = int(page_number)
    except:
        print("Page number must be a integer number")
        return
    
    if page_numbers < 0: 
        print("Page number can't be negative!")
        
    try:
        with open ('Available_Books.txt','w+') as file:
            book_entry= f'{book_name}-Page Number {page_number} \n'
            file.write(book_entry)
    except Exception as e:
        print(e)