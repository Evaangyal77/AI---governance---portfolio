# Simple data anonymization example
# Purpose: demonstrate basic data privacy concepts

import pandas as pd

data = {
    "name": ["Anna", "Béla", "Csilla"],
    "email": ["anna@email.com", "bela@email.com", "csilla@email.com"],
    "age": [28, 35, 42]
}

df = pd.DataFrame(data)

# Anonymize personal data
df["name"] = "REDACTED"
df["email"] = "REDACTED"

print(df)
