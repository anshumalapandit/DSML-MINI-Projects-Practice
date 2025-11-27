import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Datasets/Datasets/IRIS.csv")
print("Dataset loaded")
print(df.dtypes)
numerics=df.select_dtypes(include=['int64','float64']).columns.tolist()
cat=df.select_dtypes(include=['object']).columns.tolist()

print(numerics)
print(cat)

# creating histograms for each 
# histograms for only numerics 
for num in numerics:
    # remember i wantt histogram for each feature 
    # u r doing df.hist pagal it will creat hist for all na do df[num].hist
    df[num].hist(figsize=(15,12),bins=20)
    plt.title("Histogram for"+num)
    plt.xlabel(num)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
