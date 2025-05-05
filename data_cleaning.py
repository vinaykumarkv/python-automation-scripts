import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('input_data.csv')

# Step 2: Clean the data (e.g., remove missing values)
df_cleaned = df.dropna()

# Step 3: Save the cleaned data to a new file
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("Data cleaned successfully and saved as 'cleaned_data.csv'")