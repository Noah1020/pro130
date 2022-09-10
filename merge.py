import csv
import pandas as pd


df = pd.read_csv("brown_dwafs.csv")

df = df.dropna()

df["radius"] = df["radius"] * 0.102763 


df['mass']=df['mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')


df["mass"] = df["mass"] * 0.000954588  



df.to_csv("new_dwafs.csv")


data1 = []
data2 = []


with open("new_dwafs.csv", "r", encoding="utf8")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)


headers1 = data1[0]
planet_data = data1[1:]



with open("stars.csv", "r", encoding = "utf8")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers2 = data2[0]
stars_data = data2[1:]


headers = headers1 + headers2
new_data = []

for index,data in enumerate(stars_data):
    new_data.append(planet_data[index] + stars_data[index])

with open("final_data.csv", "a+", encoding= "utf8")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(new_data)



