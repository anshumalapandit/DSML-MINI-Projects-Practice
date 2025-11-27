import pandas as pd
import matplotlib.pyplot as plt
# load the dataset
df=pd.read_csv("Datasets/Datasets/House Data.csv")
print("dataset loaded")
num_var=df.select_dtypes(include=['int64','float64']).columns.tolist()
print(num_var)
for num in num_var:
    # creating hist for each faeture
    print("Mean ",df[num].mean())
    print("Minimum ",df[num].min())
    print("Maximum ",df[num].max())
    print("Variance ",df[num].var())
    print("Median ",df[num].median())
    print("Standard dev: ",df[num].std())
    print("Quantile ",df[num].quantile(0.25))
    df[num].hist(figsize=(10,10),bins=10)
    plt.tight_layout()
    plt.show()
