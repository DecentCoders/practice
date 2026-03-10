import colors
def avail_books():
    print(f"{colors.GREEN}-----Available Books----{colors.RESET}")
    try:  
        with open ("Available_Books.txt","r") as file:
            avail_books_list = file.readlines()
            for line in avail_books_list:
                print(line.strip())
    except:
        print("something is wrong")