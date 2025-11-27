import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

#  step 1 load and remove 1st column id
df=pd.read_csv("Datasets/Datasets/Lipstick.csv")
df=df.drop("Id",axis=1)
# now make independent var and dependent var
X=df[["Age","Income","Gender","Ms"]]
Y=df["Buys"]
# now i will apply one hot encoding
ohe=OneHotEncoder(handle_unknown="ignore",sparse_output=False)
# now fit the traning data
X_encoded=ohe.fit_transform(X)
# now transform the output ko
test_dict={
    "Age":"21-35",
    "Income":"Low",
    "Gender":"Male",
    "Ms":"Married"
}
test_data=pd.DataFrame([test_dict])
# now transform it finally
Y_encoded=ohe.transform(test_data)
# now train ur model
model=DecisionTreeClassifier()
model.fit(X_encoded,Y)
# now prediction kro
prediction=model.predict(Y_encoded)[0]
print("prediction is: ",prediction)
