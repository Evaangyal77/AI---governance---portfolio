# Simple data quality check example
# Purpose: demonstrate basic data quality concepts (missing values)

import pandas as pd

data = {
    "user_id": [1, 2, 3, 4],
    "age": [25, None, 40, None],
    "country": ["HU", "DE", None, "FR"],
}

df = pd.DataFrame(data)

# Check missing values
missing_values = df.isnull().sum()

print("Missing values per column:")
print(missing_values)
