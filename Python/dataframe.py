import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
# Display the DataFrame
print("Original DataFrame:")
print(df)