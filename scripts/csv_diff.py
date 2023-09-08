import pandas as pd
import time
import os

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **             This Joetility is the Website Reacher!             **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        * This Joetility will compare the first column from two csv files  *\n"
      "        * and print out (to the screen) the discrepancies between each!    *\n"
      "        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **\n")

time.sleep(3)

def compare_csv_files(csv_file1, csv_file2):
    # Read the CSV files
    df1 = pd.read_csv(csv_file1)
    df2 = pd.read_csv(csv_file2)

    # Get the first column from each DataFrame
    col1 = df1[df1.columns[0]]
    col2 = df2[df2.columns[0]]

    # Find values that are in the first column of the first DataFrame but not the second
    missing_in_second = set(col1) - set(col2)

    # Find values that are in the first column of the second DataFrame but not the first
    missing_in_first = set(col2) - set(col1)

    print('Values in first column of first CSV that are not in the first column of second CSV:')
    for val in missing_in_second:
        print(val)

    print('Values in first column of second CSV that are not in the first column of first CSV:')
    for val in missing_in_first:
        print(val)
csv1 = input("Enter first CSV filename with the extension: ")
csv2 = input("Enter second CSV filename with the extension: ")

if __name__ == "__main__":
    compare_csv_files(csv1, csv2)
    
