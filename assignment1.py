import pandas as pd
df=pd.read_csv("Datasets/Datasets/Titanic.csv")
# indexing and selecting
print(df.dtypes)
# select one feature
print(df["Age"].head())
# selecting more than one feature
print(df[["Age","Sex"]].head())
# selecting row iloc 
# first 5 rows dega 0 to 4
print(df.iloc[0:5])
print(df.loc[df["Age"]>10])
print(df.sort_values("Age",ascending=False))
print(df.describe(include="all"))

