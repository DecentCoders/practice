import colors
def avail_books():
    print(f"{colors.GREEN}-----Available Books----{colors.RESET}")
    with open ("Available_Books.txt","r") as file:
        avail_books_list = file.readlines()
        print(avail_books_list.strip())