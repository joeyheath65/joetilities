import pandas as pd

print("Joe's CSV Diff Utility!"
      "***   USAGE NOTE   ***"
      "This utility will compare the first column of 2 .csv files and print out"
      "which lines are not present in CSV2 that ARE present in CSV1 and vice versa.")

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
    
