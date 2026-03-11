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
            while True:
                try:
                    user_choice =input("Enter the Desired books number: ").strip()
                    choice_index = int(user_choice) - 1
                    if 0 <= choice_index <= len(book_entries):
                        selected_book = book_entries[choice_index]
                        break
                    else:
                        print(f'input number from 1 to {len(book_entries)}')
                except ValueError:
                    print("Please enter a valid number!")  
                         
            try:
                book_name, pages, price = [part.strip() for part in selected_book.split("~")]
            except Exception as e:  
                print(e)
                return
                
            while True:
                confirm=input(f'Are you sure buying {book_name} with price {price} (yes or no): ')
                if confirm in ['yes','no']:
                    break
                print(f"{colors.RED}Invalid input! Enter 'yes' or 'no'.{colors.RESET}")
            if confirm == "no":
                print("purchase Cancelled..")
                return
            updated_avail_list =[header]+[b for i,b in enumerate(book_entries) if i != choice_index]
            with open('Available_Books.txt', 'w', encoding='utf-8') as file:
                file.write('\n'.join(updated_avail_list))
            with open("Booked_list.txt",'a+',encoding='utf-8') as file:
                file.seek(0)
                if not file.read().strip():
                    file.write(header+'\n')
                file.write(selected_book)
            print(f"\n{colors.GREEN}✅ Purchase confirmed!{colors.RESET}")
            print(f"📚 Book '{book_name}' has been purchased.")
            print(f"🔄 Removed from Available file and added to Booked file.")
    except FileNotFoundError as e:
        print(f"{colors.RED}Error: File not found - {e.filename}{colors.RESET}")
    except PermissionError:
        print(f"{colors.RED}Error: No permission to read/write files.{colors.RESET}")
    except Exception as e:
        print(f"{colors.RED}Unexpected error: {type(e).__name__} - {e}{colors.RESET}")
if __name__ =="__main__":
    purchase_books()