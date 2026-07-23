import pandas as pd
df = pd.read_csv("sample_table.csv")
df["Salary"] = [1000,1000,1234,1234,4120]
print(df.isnull())
print(df.fillna("america"))
print(df.rename({"Name":"Name2345"}))
print(df.groupby("ID")["Age"].sum())
