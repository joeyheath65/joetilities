import os
import time

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **                  ---> M A I N  M E N U <---                    **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()


time.sleep(5)
print()
def show_menu():
    print("    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
          "    *                    J O E T I L I T I E S!                       *\n"
          "    *                       M A I N  M E N U                          *\n"
          "    *            Please select a Joetility to run from                *\n"
          "    *             the menu below and enjoy the magic!                 *\n"
          "    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    print()
    print("     1. Joe's Site Reachability Checker")
    print("     2. Joe's Web Scraper")
    print("     3. Joe's Desktop Cleaner Upper")
    print("     4. Joe's CSV differ")
    print("     9. Exit")
    print()
    
# menu choices here, add elif statement for more choices
def run_script(choice):
    if choice == "1":
        os.system("python3 joetilities/reachable.py")
    elif choice == "2":
        os.system("python3 joetilities/sitescrape.py")
    elif choice == "3":
        os.system("python3 joetilities/desktopclear.py")
    elif choice == "4":
        os.system("python3 joetilities/csv_diff.py")    

def main():
    while True:
        os.system('clear')
        show_menu()
        user_choice = input("---> Enter your choice: ")
        if user_choice == "9":
            print("Exiting...")
            break
        run_script(user_choice)

if __name__ == "__main__":
    main()
