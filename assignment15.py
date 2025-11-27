"""
15. Use the dataset 'titanic'. The dataset contains 891 rows and contains
 information about the passengers who boarded the unfortunate Titanic
 ship. Use the Seaborn library to see if we can find any patterns in the data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Datasets/Datasets/Titanic.csv")

print("Dataset loaded")

print(df.dtypes)
print(df.info())
print(df.describe())

# next kya karu bro
#  overall survival
sns.countplot(x="Survived",data=df)
plt.title("Overall Survival")
plt.tight_layout()
plt.show()
# survival by gender
sns.countplot(x="Sex",hue="Survived",data=df)
plt.title("Survival count by gender")
plt.tight_layout()
plt.show()
# survival by Pclass
sns.countplot(x="Pclass",hue="Survived",data=df)
plt.title("Survival count by Pclass")
plt.tight_layout()
plt.show()
# histogram 
sns.histplot(df["Age"].dropna(),kde=True)
plt.title("Age Distribution ")
plt.tight_layout()
plt.show()
#boxplot 
sns.boxplot(x="Survived",y="Age",data=df)
plt.title("Age vs Survival")
plt.tight_layout()
plt.show()
# heatmap
sns.heatmap(df.isnull(),cbar=True)
plt.title("Missing Values Overall")
plt.tight_layout()
plt.show()