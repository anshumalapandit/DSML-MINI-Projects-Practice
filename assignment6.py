import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
#   load the dataset
df=pd.read_csv("Datasets/Datasets/Lipstick.csv")
print("Dataset Loaded") 
# step 1: drop column 1
df=df.drop("Id",axis=1)
# step 2:  store input in X , and target var in Y
X=df[["Age","Income","Gender","Ms"]]
Y=df["Buys"]
# step 3: apply one
ohe=OneHotEncoder(handle_unknown="ignore",sparse_output=False)
# traning data ko fit kro
X_encoded=ohe.fit_transform(X)
#  now test data pr transofrm kro
test_dict={
    "Age":">35",
    "Income":"Medium",
    "Gender":"Female",
    "Ms":"Married"
}
test_data=pd.DataFrame([test_dict])
# now transform the test_data
Y_encoded=ohe.transform(test_data)

# now trained the model 
model=DecisionTreeClassifier()
model.fit(X_encoded,Y)

# prediction kro
prediction=model.predict(Y_encoded)[0]
print("Prediction: ",prediction)
