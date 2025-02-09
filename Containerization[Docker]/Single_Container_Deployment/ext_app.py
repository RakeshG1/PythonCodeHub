import pandas as pd

# Path to the mounted CSV file inside the container
csv_file_path = '/app/dummy.csv'

# Reading the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the DataFrame (you can modify this part as needed)
print(df)