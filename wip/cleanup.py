import pandas as pd

def combine_duplicates_in_csv(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Group by the first column and sum the other columns
    df = df.groupby(df.columns[0]).sum().reset_index()

    # Write the result back to the CSV file
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    combine_duplicates_in_csv('mcm_executed.csv')
