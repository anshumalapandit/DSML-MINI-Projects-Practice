import pandas as pd
import math 

df=pd.read_csv("Datasets/Datasets/Lipstick.csv")
print("dataset loaded")
# step1 : remove first column , last target class bcoz not needed 
df=df.drop("Id",axis=1)
print("dropped")
# Convert DataFrame rows to list-of-lists (easy to work without pandas methods)
data=df.values.tolist()
# exclude last column keep only 4 age,income,gender,ms
features=df.columns[:-1].tolist() # all except target column , 

# entropy function
def entropy(rows):
    total=len(rows)
    yes=sum(1 for r in rows if r[-1]=="Yes")  # yaha pe ander wale yes ko "" iske ander enclosed krna mtlb bhulna
    no=sum(1 for r in rows if r[-1]=="No")  # pagal ladki jo dataset mai Yes No hai wo likh

    if(yes==0 or no==0):
        # its means belonging to same class =pure hai
        return 0
    
    # calculate probabilities
    p_yes=yes/total
    p_no=no/total

    return -p_yes*math.log2(p_yes)-p_no*math.log2(p_no)

# information gain function
def info_gain(rows,colIdx):
    parent=entropy(rows)
    total=len(rows)
    # create empty grp/dict jisme instances stores karenge
    group={}
    for r in rows:
        val=r[colIdx]  # e.g mujhe 0 , whether ka info gain nikalna hai
        if val not in group:
        # if wheter is not present in group, iska instance store nhi hai to grp banalo
          group[val]=[]
        group[val].append(r) # ek ek karke sare instances store hote jayenge 
    
    # sv/s hota hai wo calculate karenge
    weighted=0
    # hamre array of array pe iterate karna hai group dict hai usme se values array hai , values ko nikalo 
    for g in group.values():
        weight=len(g)/total
        weighted+=weight*entropy(g)
    
    # information gain calculate karenge
    gain=parent-weighted

    return gain
print("Done")

print("\n--- Information Gain of Each Feature ---")

ig_age = info_gain(data, 0)
print("Age =", round(ig_age,4))

ig_income = info_gain(data, 1)
print("Income =", round(ig_income,4))

ig_gender = info_gain(data, 2)
print("Gender =", round(ig_gender,4))

ig_ms = info_gain(data, 3)
print("Marital Status =", round(ig_ms,4))

ig_list = [ig_age, ig_income, ig_gender, ig_ms]

rootNode=max(ig_list)

print("max=", rootNode)
print("Root Node: is AGE")


    
