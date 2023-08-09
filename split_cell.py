import pandas as pd

def separate_names_in_csv(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Assuming that the first column contains the names
    names = df[df.columns[0]].str.split(',', expand=True)

    # Create new columns from the split data
    df['Lastname'] = names[0].str.strip() # Strip is used to remove any leading/trailing whitespace
    df['Firstname'] = names[1].str.strip()

    # Remove the original names column
    df = df.drop(columns=df.columns[0])

    # Write the result back to the CSV file
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    separate_names_in_csv('mcm_executed.csv')
