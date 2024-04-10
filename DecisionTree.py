import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


data=pd.read_csv('train.csv')
Y=data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X=data[feature_columns]


model=DecisionTreeRegressor()
model.fit(X,Y)

# print("predeicted value : ",model.predict(X.head()))
# print("the real value are ",Y.head().tolist())

X_train,X_val,Y_train,Y_val=train_test_split(X,Y,random_state=1)

model1=DecisionTreeRegressor(random_state=1)
model1.fit(X_train,Y_train)
val_predicted=model1.predict(X_val)
# print(val_predicted[:5])
# print(mean_absolute_error(val_predicted,Y_val))

# calculating error
def MeanAbsoluteError(max_leaf_nodes,X_train,Y_train,X_val,Y_val):
    model=DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes,random_state=1)
    model.fit(X_train,Y_train)
    predictedValues=model.predict(X_val)
    mae=mean_absolute_error(predictedValues,Y_val)
    return mae




candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
best_size=max(candidate_max_leaf_nodes)
errors=[]



for leaf in candidate_max_leaf_nodes:
    error=MeanAbsoluteError(leaf,X_train,Y_train,X_val,Y_val)
    if(errors):
     if(error < min(errors)):
        best_size=leaf
        print("best size = ",best_size)

    errors.append(error)    
    print("errors array :",errors)
    
    

        
