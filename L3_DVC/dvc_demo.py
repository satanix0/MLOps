import pandas as pd
import os
# Create a sample original DataFrame with column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Adding new row to df for V2 of data
<<<<<<< HEAD
new_row_loc = {'Name': 'Dennis', 'Age': 20, 'City': 'Cityl'}
=======
<<<<<<< HEAD
new_row_loc = {'Name': 'V2', 'Age': 20, 'City': 'Cityl'}
=======
new_row_loc = {'Name': 'Dennis', 'Age': 20, 'City': 'Cityl'}
>>>>>>> aaed43a52246dfb25e78875443b75f5c66458448
>>>>>>> 2d4e62b093111ef7b9370db0b9b67c9110476ac0
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3 of data
new_row_loc2 = {'Name': 'Riley', 'Age': 30, 'City': 'Cityl'}
df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exists at the root level
data_dir = 'data/'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)


print(f"CSV file saved to {file_path}")
