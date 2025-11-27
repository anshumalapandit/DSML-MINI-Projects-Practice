"""
 5. Write a program to do: A dataset collected in a cosmetics shop showing
 details of customers and whether or not they responded to a special offer
 to buy a newlip-stick is shown in table below. (Use library commands)
 According to the decision tree you have made from the previous training
 data set, what is the decision for the test data: [Age < 21, Income = Low,
 Gender = Female, Marital Status = Married]
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

df=pd.read_csv("Datasets/Datasets/Lipstick.csv")
print("Datasets Loaded")
df=df.drop("Id",axis=1) # why we are removing bcoz its useless for the model, it is unique id it has no pattern ,it will confuse it to the model.
# stores input in X and target var ko in y
# X = independent variable / predictors 
X=df[["Age","Income","Gender","Ms"]]
# y= dependent variable ,output 
Y=df["Buys"]

# apply one hot encoder 
#handle_unknown ? If test input contains a category that was NOT present in training → error nahi haiga.
ohe=OneHotEncoder(handle_unknown="ignore",sparse_output=False)
# fit on tranind data
X_encoded=ohe.fit_transform(X)
# sparse ? Data is returned as simple array, not sparse matrix → easy to print & understand. 
test_dict={
    "Age": "<21",
    "Income":"Low",
    "Gender":"Female",
    "Ms":"Married"
}

test_data=pd.DataFrame([test_dict])
# now encode the test set just in a same way u did for input one
#  very very very very imp anshu, yaha pe ohe.transform(test_data)
Y_encoded=ohe.transform(test_data)
# now i will train my model
model=DecisionTreeClassifier()
model.fit(X_encoded,Y)
#  now i will perform prediction
prediction=model.predict(Y_encoded)[0]
print("pura prediction: ",prediction)
print("Prediction for test data: ",prediction)


