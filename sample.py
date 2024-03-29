import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane'],
        'Age': [25, 30]}
df = pd.DataFrame(data)

# View the first few rows
print(df.head())