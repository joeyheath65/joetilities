import os
import shutil
import time

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **          This Joetility is the Desktop Cleaner Upper!          **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        *  This Joetility will move desktop clutter into a folder called   *\n"
      "        *           (wait for it.....) ------>  Desktop2!!!!!              *\n"
      "        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **\n")

time.sleep(2)

print("Cleaning up your desktop now....\n")
time.sleep(2)

def move_files(source_folder, destination_folder):
    # Get a list of files in the source folder
    source_files = os.listdir(source_folder)
    
    for file_name in source_files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        
        # Check if the file already exists in the destination folder
        if not os.path.exists(destination_path):
            # Move the file to the destination folder
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination_folder}")
        else:
            print(f"{file_name} already exists in {destination_folder}")

if __name__ == "__main__":
    source_folder = "/Users/joehome/Desktop"
    destination_folder = "/Users/joehome/Desktop2"
    
    move_files(source_folder, destination_folder)
    print("And like magic....its done!\n")
    print()
    print("Heading back to the Main Menu....")
    time.sleep(2)
    
