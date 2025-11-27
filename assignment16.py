"""
 16. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
 contains information about the passengers who boarded the unfortunate
 Titanic ship. Write a code to check how the price of the ticket (column
 name: 'fare') for each passenger is distributed by plotting a histogram
"""
import pandas as pd
import matplotlib.pyplot as plt

# dataset
df=pd.read_csv("Datasets/Datasets/Titanic.csv")
print("Dataset loaded")

# df.hist(column="Fare",figsize=(15,12),bins=20)
df["Fare"].hist(figsize=(10,10),bins=20)
plt.title("Distribution of price for each passenger")
plt.tight_layout()
plt.show()