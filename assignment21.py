import pandas as pd
import math
import random
# step 1 : load the dataset
df=pd.read_csv("Datasets/Datasets/IRIS.csv")
# craeting points datapoints for sepal_length,sepal_width
points=list(zip(df["sepal_length"],df["sepal_width"]))
# step 2 randomly initialise 4 medoids 
m1,m2,m3,m4=random.sample(points,4)
#  distance formula
def distance(p,m):
    return ((p[0]-m[0])**2+ (p[1]-m[1])**2)**0.5
# step 3: now calculate distance of each data points from each med
#  now K means will run atleats 10 times
for it in range(10):
    # define 3 cluster 
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    for p in points:
        d1=distance(p,m1)
        d2=distance(p,m2)
        d3=distance(p,m3)
        d4=distance(p,m4)
        # now whoevery distance small assigned to that respective cluster

        d=min(d1,d2,d3,d4)
        if(d==d1):
            c1.append(p)
        elif(d==d2):
            c2.append(p)
        elif(d==d3):
            c3.append(p)
        else:
            c4.append(p)
        
        # now update the centroids
        # safer check har cluster mai dps hai n atleast
        if(len(c1)>0):
            x1=sum(p[0] for p in c1)/len(c1)
            y1=sum(p[1] for p in c1)/len(c1)
            m1_new=(x1,y1)
        else:
            m1_new=m1
        
        if(len(c2)>0):
            x2=sum(p[0] for p in c2)/len(c2)
            y2=sum(p[1] for p in c2)/len(c2)
            m2_new=(x2,y2)
        else:
            m2_new=m2
        if(len(c3)>0):
            x3=sum(p[0] for p in c3)/len(c3)
            y3=sum(p[1] for p in c3)/len(c3)
            m3_new=(x3,y3)
        else:
            m3_new=m3
        if(len(c4)>0):
            x4=sum(p[0] for p in c1)/len(c4)
            y4=sum(p[1] for p in c1)/len(c4)
            m4_new=(x4,y4)
        else:
            m4_new=m4

# lets print the result 
print("Updated m1 : ",m1_new)
print("Updated m2 : ",m2_new)
print("Updated m3 : ",m3_new)
print("Updated m4 : ",m4_new)
print("Final Clusters c1 size: ",len(c1))
print("Final Clusters c2: ",len(c2))
print("Final Clusters c3: ",len(c3))
print("Final Clusters c4: ",len(c4))
# 
        
        
