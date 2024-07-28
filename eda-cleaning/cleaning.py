import pandas as pd
import os

os.getcwd()

df = pd.read_csv("Users/rohankrishnan/Downloads/Indicator_Input_Values_20240726.csv")

df

df1 = pd.read_csv("Users/rohankrishnan/Downloads/GDPC1.csv")

df1.dtypes

df1['DATE'] = pd.to_datetime(df1['DATE'])
df1["Year"] = df1["DATE"].dt.year
df1["Month"] = df1["DATE"].dt.month

df1.to_csv("Users/rohankrishnan/Downloads/GDPC1New.csv")

new = df.merge(df1, how = "left", on =  ["Year", "Month"])

df2 = pd.read_csv("Users/rohankrishnan/Downloads/UNRATE.csv")
df2["DATE"] = pd.to_datetime(df2["DATE"])
df2["Year"] = df2["DATE"].dt.year
df2["Month"] = df2["DATE"].dt.month

new = new.merge(df2, how = "left", on = ["Year", "Month"])
new = new.drop(["DATE_x", "DATE_y"], axis = 1)

df3 = pd.read_csv("Users/rohankrishnan/Downloads/CSUSHPINSA.csv")
df3["DATE"] = pd.to_datetime(df3["DATE"])
df3["Year"] = df3["DATE"].dt.year
df3["Month"] = df3["DATE"].dt.month

new = new.merge(df3, how = "left", on = ["Year", "Month"])

df4 = pd.read_csv("Users/rohankrishnan/Downloads/FEDFUNDS.csv")
df4["DATE"] = pd.to_datetime(df4["DATE"])
df4["Year"] = df4["DATE"].dt.year
df4["Month"] = df4["DATE"].dt.month

new = new.merge(df4, how = "left", on = ["Year", "Month"])
new = new.drop(["DATE_x", "DATE_y"], axis = 1)

df5 = pd.read_csv("Users/rohankrishnan/Downloads/MEDCPIM158SFRBCLE.csv")
df5["DATE"] = pd.to_datetime(df5["DATE"])
df5["Year"] = df5["DATE"].dt.year
df5["Month"] = df5["DATE"].dt.month

new = new.merge(df5, how = "left", on = ["Year", "Month"])
new = new.rename({"MEDCPIM158SFRBCLE":"MEDIANCPI"}, axis = 1)

electionYear = []
eYearCheck = [2004, 2008, 2012, 2016, 2020, 2024]
for i in df["Year"]:
    if i in eYearCheck:
        electionYear.append(1)
    else: 
        electionYear.append(0)
        
        
new["ElectionYear"] = electionYear



