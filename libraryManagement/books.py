import colors
def avail_books():
    print(f"{colors.GREEN}-----Available Books----{colors.RESET}")
    try:  
        with open ("Available_Books.txt","r") as file:
            avail_books = file.readlines()
            header = avail_books[0]
            avail_book_list = avail_books[1:]
            if not avail_book_list:
                print(f"{colors.RED}Sorry no book available right now{colors.RED}")
                return
            print(f'{colors.BLUE}{header}{colors.RESET}',end='')
            for index, line in enumerate(avail_book_list):
                print(f'{colors.YELLOW}{index+1}: {colors.RESET}{line.strip()}')
    except:
        print(f"{colors.RED}something is wrong {colors.RESET}")