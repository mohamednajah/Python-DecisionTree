from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd 


data=pd.read_csv('train.csv') 

y=data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X=data[feature_columns]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=1)
Model=RandomForestRegressor(random_state=1)
Model.fit(X_train,y_train)

predictedValues=Model.predict(X_test)
print("Mean absolute Error :{}".format(mean_absolute_error(predictedValues,y_test)))



