import csv
import pandas as pd


df = pd.read_csv("final_data.csv")

print(df.shape)

del df["Unnamed: 0"]
del df["index"]
del df["index1"]


print(df.shape)

df = df.dropna()

print(df.shape)



df.to_csv("project130.csv")


