# Convert a Row to a Column Header in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'experience': [10, 13, 15],
    'salary': [175.1, 180.2, 190.3],
})

print(df)

df.columns = df.iloc[1]

print('-' * 50)

print(df)
