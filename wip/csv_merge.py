import pandas as pd

def merge_csv_files(csv_files, output_file):
    # Initialize an empty list to hold DataFrames
    dfs = []

    # Read each CSV file and append it to the list
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dfs.append(df)

    # Concatenate all DataFrames in the list
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    csv_files = ['standenk-cml1-stats.csv', 'jralls-cml1-stats.csv', 'bfsamz-cml1-stats.csv', 'sccros-cml1-stats.csv', 'joseheat-cml1-stats.csv', 'davbrig-cml1-stats.csv', 'iqbalmal-cml1-stats.csv']
    output_file = 'merged.csv'
    merge_csv_files(csv_files, output_file)