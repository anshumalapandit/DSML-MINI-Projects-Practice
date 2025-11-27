import pandas as pd
import math

# step 1: Load the dataset 
data = {
    "Age": ["Young","Young","Middle","Old","Old","Old","Middle","Young","Young","Old","Young","Middle","Middle","Old"],
    "Income": ["High","High","High","Medium","Low","Low","Low","Medium","Low","Medium","Medium","Medium","High","Medium"],
    "Married": ["No","No","No","No","Yes","Yes","No","No","Yes","Yes","Yes","No","Yes","No"],
    "Health": ["Fair","Good","Fair","Fair","Fair","Good","Good","Fair","Fair","Fair","Good","Good","Fair","Good"],
    "Class": ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]
}

df=pd.DataFrame(data)
print("Dataset Loaded")
rows=df.values.tolist() # for pandas operation easier
#  step 2 : 
#  craete frequency table
freq=pd.crosstab(df["Age"],df["Class"])
print("Frequency table Ags vs Class")
print(freq)

#  entropy fxn
def entropy(rows):
    total=len(rows)
    yes =sum(1 for r in rows if r[-1]=="Yes")
    no=sum(1 for r in rows if r[-1]=="No")
    # edge cases
    if(yes==0 or no==0):
        return 0
    # calculate probabiltit
    p_yes=yes/total
    p_no=no/total

    return -p_yes*math.log2(p_yes)-p_no*math.log2(p_no)
# information gain fxn
def info_gain(rows,col_idx):
    # first task is to calculate parent entropy
    parent=entropy(rows)
    total=len(rows)
    # dont forget to create empty dict/group
    groups={}
    for r in rows:
        val=r[col_idx]
        if val not in groups:
            # craete empty box
            groups[val]=[]
        # then append it to the groups
        groups[val].append(r)
    
    # now calculate weighted
    # abb sare instance store ho gye now calculate weighted the second part of the formula
    weighted=0
    for g in groups.values():
        weight=len(g)/total
        weighted+=weight*entropy(g)

    gain=parent-weighted
    return gain

# calculate IG and entropy 
print("Entropy Before split of age : ",round(entropy(rows),2))
print("Information Gain for splitting on Age: ",info_gain(rows,0))
