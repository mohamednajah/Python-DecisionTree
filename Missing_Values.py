import pandas as pd
from sklearn.metrics  import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer


##################initialization########################
data=pd.read_csv("melb_data.csv")
Y=data.Price
melbourne=data.drop(["Price"],axis=1)
X =melbourne.select_dtypes(exclude=['object'])
missing_values=X.isnull().sum()
print(missing_values)

X_train,X_test,y_train,y_test=train_test_split(X,Y)

columns_missing_values=[col for col in data.columns
                        if data[col].isnull().any()]



###################Calculate the score of the model ###############
def score_model(x_train=X_train,x_test=X_test,y_train=y_train,y_test=y_test):
    Forest=RandomForestRegressor()
    Forest.fit(x_train,y_train)
    predictedValues=Forest.predict(x_test)
    mae=mean_absolute_error(predictedValues,y_test)
    return mae;




#################First approach  : drop colums which contains null values ################
#X_train=data.drop(columns_missing_values,axis=1)
#X_test=data.drop(columns_missing_values,axis=1)
#print(score_mdeol())



#######################Second approach : imputation ########
impute=SimpleImputer()

imputed_X_train=pd.DataFrame(impute.fit_transform(X_train))
imputed_X_test=pd.DataFrame(impute.transform(X_test))


imputed_X_train.columns=X_train.columns
imputed_X_test.columns=X_test.columns

# print(score_model(imputed_X_train,imputed_X_test))