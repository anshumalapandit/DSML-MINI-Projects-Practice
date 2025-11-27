# step 1: defien all dps
p1=(2,10)
p2=(2,5)
p3=(8,4)
p4=(5,8)
p5=(7,5)
p6=(6,4)
p7=(1,2)
p8=(4,9)

all_points=[p1,p2,p3,p4,p5,p6,p7,p8]

# step 2:
m1=p1
m2=p4
m3=p7

c1=[]
c2=[]
c3=[]

# distance function
def distance(p,m):
    return ((p[0]-m[0])**2 + (p[1]-m[1])**2)**0.5
# calculate distance of all dps from m1,m2,m3
for p in all_points:
    d1=distance(p,m1)
    d2=distance(p,m2)
    d3=distance(p,m3)

    # now whoever distance is less assign in that cluster
    if(d1<=d2 and d1<=d3):
        c1.append(p)
    elif(d2<=d1 and d2<=d3):
        c2.append(p)
    else:
        c3.append(p)

# now update the value of m1,m2,m3
#  but before check tino cluster mai dps hai ki nhi tabhi new medoit calculate kar paoge na
if len(c1)>0:
    x1=sum(p[0] for p in c1) / len(c1)
    y1=sum(p[1] for p in c1) / len(c1)
    m1_new=(x1,y1)
else:
    m1_new =m1 # assigned old cluster only

if len(c2)>0:
    x2=sum(p[0] for p in c2) / len(c2)
    y2=sum(p[1] for p in c2) / len(c2)
    m2_new=(x2,y2)
else:
    m2_new =m2 # assigned old cluster only

if len(c3)>0:
    x3=sum(p[0] for p in c3) / len(c3)
    y3=sum(p[1] for p in c3) / len(c3)
    m3_new=(x3,y3)
else:
    m3_new =m3 # assigned old cluster only

print("cluster 1",c1)
print("cluster 2",c2)
print("cluster 3",c3)

# 1] Which cluster does P6 belong to? 
ans1="c1" if p6 in c1 else ("c2"  if p6 in c2 else "c3")
print("p6 belongs to ",ans1)
print("what is the population of a cluster around m3 ", len(c3))
print("updated values of m1: ",m1_new)
print("updated values of m2: ",m2_new)
print("updated values of m3: ",m3_new)


