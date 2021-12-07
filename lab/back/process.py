import pandas as pd
import numpy as np
import sklearn
import os
from sklearn.model_selection import train_test_split
import statsmodels.api as st
import mysql.connector as db


def logModel(column,x_train, y_train):
    st_model = st.OLS(y_train,x_train[column])
    _model_ = st_model.fit()
    return _model_
#---------------------------------------------------

def writeF(where, what):
    print("**********************") 
    print("\nwhere\n") 
    print(where) 
    print("\nwhat\n")
    print(what) 
    print("*********************")
    arquivo = open(where,'w+')
    arquivo.writelines(what)
    arquivo.close()

#---------------------------------------------------
def tratamento(file) :
    path = os.environ['dataset']
    print ("*****")
    print (os.environ['dataset'])
    from sklearn.model_selection import train_test_split
    import statsmodels.api as st
    data = pd.read_csv(path+file)
    data.describe()
    data.info()
    data[data['Number of Doors'].isna() == True] = 0
    data[data['Engine HP'].isna() == True] = 0
    data[data['Engine Cylinders'].isna() == True] = 0
    data[data['highway MPG'].isna() == True] = 0
    data[data['city mpg'].isna() == True] = 0
    data[data['Popularity'].isna() == True] = 0
    dummy = data[['Make',
    'Engine Fuel Type',
    'Transmission Type',
    'Driven_Wheels' ,
    'Market Category',
    'Vehicle Size',
    'Vehicle Style',]]

    strings = data[['Year',
    'Engine HP',
    'Engine Cylinders',
    'Number of Doors',
    'highway MPG',
    'city mpg',
    'Popularity'
                            ]]
    target = data[["MSRP"]]
    dm = pd.get_dummies(dummy,
            prefix_sep='_',
            drop_first=True
    )
    data_base = pd.concat([dm,strings], axis = 1 )


    y_train, y_test, x_train, x_test = train_test_split(target,data_base, test_size = 0.3, random_state = 42)
    x_train.shape, x_test.shape, y_train.shape, y_test.shape

    _continue_ = True
    _modelo_ = None


    x_train = st.add_constant(x_train, True)
    columns = x_train.columns.values.tolist()
    while _continue_:
            modelo = logModel(columns, x_train, y_train)
            menor = 0.07000
            rem = ""
            _encontrou_ = False
            for i in columns:
                    if round(float(modelo.pvalues[i]),5) < 0.7 and round(float(modelo.pvalues[i]),5) < menor and i != "const" :
                            menor = modelo.pvalues[i]
                            rem = i
                            _encontrou_ = True

            if _encontrou_ == False:
                    print("Parando o modelo")
                    _continue_ = False
            else:
                    print(f"Remover {rem}")
                    columns.remove(rem)
            _modelo_ = modelo
    return _modelo_
        
            
