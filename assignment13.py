import pandas as pd
df=pd.read_csv("Datasets/Datasets/Covid Vaccine Statewise.csv")
print("Dataset loaded")
# Describe the dataset
print(df.dtypes)
print(df.info())
print(df.describe())

#   Number of persons state wise vaccinated for first dose in India
first_dose=df.groupby("State")["First Dose Administered"].max()
sec_dose=df.groupby("State")["Second Dose Administered"].max()

print(first_dose)
print(sec_dose)
