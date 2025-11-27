"""
19. Write a Python program to display some basic statistical details like
 percentile, mean, standard deviation etc (Use python and pandas
 commands) the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
 of iris.csv dataset
"""
import pandas as pd
df=pd.read_csv("Datasets/Datasets/IRIS.csv")
print("Dataset loaded")
print(df.dtypes)
num_var=df.select_dtypes(include=['int64','float64']).columns.tolist()
print(num_var)
cat_var=df.select_dtypes(include=['object']).columns.tolist()
print(cat_var)
speciesList=df["species"].unique()

for sp in speciesList:
    # stattistics for each species
    # filtered species uniquely row wise
    species_df=df[df["species"]==sp]
    print(species_df.min(numeric_only=True))
    print(species_df.max(numeric_only=True))
    print(species_df.median(numeric_only=True))
    print(species_df.std(numeric_only=True))
    print(species_df.var(numeric_only=True))
    print(species_df.mean(numeric_only=True))
    print(species_df.quantile([0.5,0.75,0.25],numeric_only=True))