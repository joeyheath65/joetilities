import pandas as pd

def calculate_statistics(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Calculate the average, upper percentile (90th), and lower percentile (10th)
    # Modify this to choose different columns or percentiles
    for col in df.select_dtypes(include=[pd.np.number]).columns.tolist():
        mean = df[col].mean()
        upper_percentile = df[col].quantile(0.9)
        lower_percentile = df[col].quantile(0.1)

        df[f'{col}_avg'] = mean
        df[f'{col}_90_percentile'] = upper_percentile
        df[f'{col}_10_percentile'] = lower_percentile

    # Write the result back to the CSV file
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    calculate_statistics('mcm_executed.csv')
