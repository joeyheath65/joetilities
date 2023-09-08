import time
import os

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **           This Joetility is the Network Usage Checker          **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        * This Joetility will check and print your current network usage.  *\n"
      "        *      The script will run until you stop it with a CTRL-Z         *\n"
      "        * you'll be asked if you want to add a website site to the list!!  *\n")

time.sleep(1)

print()
hostname = input("Enter the site you want to check : ")
print()
response = os.system("ping -c 1 " + hostname)
if response == 0:
  print()
  print(hostname, 'is up!')
  print()
else:
  print()
  print(hostname, 'is down!')
  print()