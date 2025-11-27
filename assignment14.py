import pandas as pd
df=pd.read_csv("Datasets/Datasets/Covid Vaccine Statewise.csv")

# describe
print(df.dtypes)
print(df.info())
print(df.describe())

# numbers of males vaccinated
male_count=df["Male(Individuals Vaccinated)"].sum()
female_count=df["Female(Individuals Vaccinated)"].sum()

print(male_count)
print(female_count)