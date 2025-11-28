import pandas as pd
df=pd.read_csv("Datasets/Datasets/Telecom Churn.csv")
print("Dataset Loaded")
print(df.dtypes)
num_var=df.select_dtypes(include=['int64','float64']).columns.tolist()
# finding statistics summary for each feature
for num in num_var:
    print("Mean for "+num,": ",df[num].mean())
    print("Minimum for "+num,": ",df[num].min())
    print("Maximum for "+num,": ",df[num].max())
    print("Variance for "+num,": ",df[num].var())
    print("Median for "+num,": ",df[num].median())
    print("Standard Deviation for "+num,": ",df[num].std())
    print("Quantile for "+num,": ",df[num].quantile(0.25))
