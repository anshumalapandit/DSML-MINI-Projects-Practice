import pandas as pd
import math
import random

# ---- STEP 1: Load IRIS dataset (take only 2 features to keep it SIMPLE) ----
df = pd.read_csv("Datasets/Datasets/IRIS.csv")
points=[]

# use only SepalLength, SepalWidth (2D points like p1=(x,y))
for i in range(len(df)):
    x = df.iloc[i, 0]   # sepal length
    y = df.iloc[i, 1]   # sepal width
    points.append((x, y))

# Make 2D points exactly like p1=(x,y) in ONE SIMPLE LINE
# points = list(zip(df["sepal_length"], df["sepal_width"]))

# ---- STEP 2: Randomly choose 3 initial centroids (as question requires) ----
m1, m2, m3 = random.sample(points, 3)

# ---- distance function (same as yours) ----
def distance(p, m):
    return ((p[0] - m[0])**2 + (p[1] - m[1])**2) ** 0.5

# ---- RUN K-means for EXACTLY 10 ITERATIONS ----
for it in range(10):

    c1 = []
    c2 = []
    c3 = []

    # assign each point to nearest centroid
    for p in points:
        d1 = distance(p, m1)
        d2 = distance(p, m2)
        d3 = distance(p, m3)

        if d1 <= d2 and d1 <= d3:
            c1.append(p)
        elif d2 <= d1 and d2 <= d3:
            c2.append(p)
        else:
            c3.append(p)

    # ---- UPDATE CENTROIDS (same style as your code) ----

    # update m1
    if len(c1) > 0:
        x1 = sum(p[0] for p in c1) / len(c1)
        y1 = sum(p[1] for p in c1) / len(c1)
        m1 = (x1, y1)

    # update m2
    if len(c2) > 0:
        x2 = sum(p[0] for p in c2) / len(c2)
        y2 = sum(p[1] for p in c2) / len(c2)
        m2 = (x2, y2)

    # update m3
    if len(c3) > 0:
        x3 = sum(p[0] for p in c3) / len(c3)
        y3 = sum(p[1] for p in c3) / len(c3)
        m3 = (x3, y3)

# ---- STEP 3: Print final clusters & means ----
print("Final Centroid m1:", m1)
print("Final Centroid m2:", m2)
print("Final Centroid m3:", m3)

print("Cluster 1 size:", len(c1))
print("Cluster 2 size:", len(c2))
print("Cluster 3 size:", len(c3))
