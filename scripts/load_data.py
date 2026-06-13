import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/creditcard.csv")

print("Dataset loaded successfully!")
print("-" * 40)

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

print("-" * 40)

# Check duplicate rows
duplicate_count = df.duplicated().sum()

print(f"Duplicate Rows: {duplicate_count}")

print("-" * 40)

# Remove duplicates
df = df.drop_duplicates()

print("After Removing Duplicates:")

print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# Save cleaned dataset
df.to_csv("data/clean/cleaned_creditcard.csv", index=False)

print("-" * 40)
print("Cleaned dataset saved successfully!")