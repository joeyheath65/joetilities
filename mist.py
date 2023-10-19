import os
import time

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **                  ---> M I S T  M E N U <---                    **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()


time.sleep(5)
print()
def show_menu():
    print("    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
          "    *                    J O E T I L I T I E S!                       *\n"
          "    *                       M I S T  M E N U                          *\n"
          "    *            Please select a Joetility to run from                *\n"
          "    *             the menu below and enjoy the magic!                 *\n"
          "    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    print()
    print("     1. Download device inventory (.json)")
    print("     2. Print Honeypot report")
    print("     3. Joe's Desktop Cleaner Upper")
    print("     4. Joe's CSV differ")
    print("     5. Joe's Network Usage Checker")
    print("     6. Joe's Single Site Checker")
    print("     9. Exit")
    print()
    
# menu choices here, add elif statement for more choices
def run_script(choice):
    if choice == "1":
        print("Executing.....")
        os.system("python3 joetilities/scripts/mist-inventory.py")
        print("Complete!!! Returning to the main menu....")
        time.sleep(3)
    elif choice == "2":
        os.system("python3 joetilities/scripts/sitescrape.py")
    elif choice == "3":
        os.system("python3 joetilities/scripts/desktopclear.py")
    elif choice == "4":
        os.system("python3 joetilities/scripts/csv_diff.py")
    elif choice == "5":
        os.system("python3 joetilities/scripts/netusage.py")        
    elif choice == "6":
        os.system("python3 joetilities/scripts/sitetest.py")    

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
