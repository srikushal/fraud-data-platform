import pandas as pd

# file path
file_path = "data/raw/creditcard.csv"

try:
    # read csv file
    df = pd.read_csv(file_path)

    print("Dataset loaded successfully!")
    print("-" * 40)

    # rows and columns
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")

    print("-" * 40)

    # column names
    print("Column Names:")
    print(df.columns.tolist())

    print("-" * 40)

    # first 5 rows
    print("First 5 Rows:")
    print(df.head())

except FileNotFoundError:
    print("File not found. Please check the file path.")

except Exception as e:
    print("Error:", e)