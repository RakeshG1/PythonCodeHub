# Import libraries
import pandas as pd

# Sample data
fruits_data = {
    "name": ["apple", "banana", "orange"],
    "cost": [10, 5, 6]
}

# Create DataFrame from the given data
df = pd.DataFrame(fruits_data)

# Display Dataframe
print(df)