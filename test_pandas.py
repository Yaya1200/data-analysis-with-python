import pandas as pd
df = pd.read_csv("sample_table.csv")
df["Salary"] = [1000,1000,1234,1234,4120]
print(df.drop("Salary", axis=1))
print(df)