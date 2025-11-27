"""
 18. Use House_Price prediction dataset. Provide summary statistics (mean,
 median, minimum, maximum, standard deviation) of variables (categorical
 vs quantitative) such as- For example, if categorical variable is age groups
 and quantitative variable is income, then provide summary statistics of
 income grouped by the age groups
"""
import pandas as pd

df=pd.read_csv("Datasets/Datasets/House Data.csv")

print(df.dtypes)
cat_var=df.select_dtypes(include=['object','category']).columns.tolist()
num_var=df.select_dtypes(include=['int64','float64']).columns.tolist()
# summary statics for numerics 
for col in num_var:
    print("Summary statistics for ", col)
    print("Minimum:",df[col].min())
    print("Maximum:",df[col].max())
    print("Variance:",df[col].var())
    print("Mean:",df[col].mean())
    print("Std Deviation:",df[col].std())
    print("Median:",df[col].median())

# summary grouped statistics for categorical Vs qualitattive
for cat in cat_var:
    for num in num_var:
        print("Summary Statistics of ",num,"Grouped by",cat)
        print(df.groupby(cat)[num].agg(["min","max","std","mean","median"]))

