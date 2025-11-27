"""
 24. Perform the following operations using Python on a suitable data set,
 counting unique values of data, format of each column, converting variable
 data type (e.g. from long to short, vice versa), identifying missing values
 and filling in the missing values.
"""
import pandas as pd

df=pd.read_csv("Datasets/Datasets/Titanic.csv")
print("Original Dataset Loaded  ")
# 1. couting unique values in each column
print(df.nunique())
# 2. format of each column data type
print("Before : ",df.dtypes)
# 3. converting variable data types from Long to short
df["Sex_Short"]=df["Sex"].map({"male": "M" , "female":"F"})
# similary converting to marital status short numeric to long label
df["Survived_Label"]=df["Survived"].map({0:"No", 1:"Yes"})
# lets convert int to string
df["Pclass"]=df["Pclass"].astype("category")
# 4.identifying the missing values
print("Missing Values",df.isnull().sum())
print("After conversion:",df.dtypes)

#  for filling with before extract num_col & cat_col
num_col=df.select_dtypes(include=['int64','float64'])
cat_col=df.select_dtypes(include=['object','category'])
#  now i will travel only specic column and fill
# i will fill num_col with median 
# and catrgorical column ko mode se fill karungi
for num in num_col:
    median_cal=df[num].median()
    df[num]=df[num].fillna(median_cal)
# Age → median se fill ✔
# Fare → median se fill ✔
for cat in cat_col:
    mode_val=df[cat].mode()[0]
    df[cat]=df[cat].fillna(mode_val)

print("After Filling Missing Values:")
print(df.isnull().sum())




