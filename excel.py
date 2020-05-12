import pandas as pd

df = pd.read_excel(r'F:\python\excel\read.xlsx',sheet_name="班级")

print(df.shape)
print("===========")

print(df)
print("===========")

print(df["人数"]>10)
print("===========")


print(df["人数"].value_counts())
print("===========")


print(df.count())
print("===========")


print(df.sum())
print("===========")
