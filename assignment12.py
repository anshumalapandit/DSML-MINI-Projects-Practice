import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("Datasets/Datasets/IRIS.csv")
print("Dataset loaded")
# check data types of each feature
print(df.dtypes)
# select numeric features and categories feature
num_df=df.select_dtypes(include=['int64','float64']).columns.tolist()
print(num_df)
# now i will iterate on this feature and plot boxplot for each
for feat in num_df:
    df.boxplot(column=feat)
    plt.title("box plot for " + feat)
    plt.tight_layout()
    plt.show()

# grouped box plot
sns.boxplot(x="species",y="petal_length",data=df)
plt.title("Grouped Box plot species vs petal length")
plt.tight_layout()
plt.show()
