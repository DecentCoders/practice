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
        return
   
    try:
        page_number = int(input("Enter the page number: ".strip()))
        if not page_number:
            print('Page number cant be empty')
            return
    except:
        print("Page number must be a integer number \n")
        return
    
    if page_number < 0: 
        print("Page number can't be negative!")
    try:
        price = int(input("Price (USD): "))
    except Exception as e:
        print("price must be a integer number")
        return
    if price <0:
        print("Price cant be negative number")
        return
        
    try:
        with open ('Available_Books.txt','a+') as file:
            book_entry= f'{book_name}-Page Number: {page_number} - Price: {price}USD \n'
            avail_test= file.readlines()
            for line in avail_test:
                if line == book_name:
                    print("The book already exists.")
                    return
            file.write(book_entry)
            print(f"{book_name} added to the inventory")
    except Exception as e:
        print(e)
        return