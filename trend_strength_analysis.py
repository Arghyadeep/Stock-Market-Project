import pandas as pd
import numpy as np
import matplotlib as plt
import pickle as pkl
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
import operator

def read_pickle(pickle_name):
    path = "pickles/"
    obj = pkl.load(open(path+pickle_name, "rb"))
    if not type(obj) == type(pd.DataFrame()):
        raise TypeError("object to read must be DataFrame")
    return obj

data = read_pickle('AAPL_tech_analysis.pkl')
#print(data.head())

def create_train_data(data):
    target1 = list(data['cci_14'])[1:] + [0]
    target2 = list(data['cci_20'])[1:] + [0]
    target3 = list(data['rsi_12'])[1:] + [0]
    target4 = list(data['rsi_6'])[1:] + [0]
    target5 = list(data['y'])[1:] + [0]

    data['t1'] = target1
    data['t2'] = target2
    data['t3'] = target3
    data['t4'] = target4
    data['t5'] = target5

    data.drop(['y'],1,inplace=True)
    data = data[1:]

    train_data = data[:-1]
    test_data = data[-1:]

    return train_data, test_data

    
train_data, test_data = create_train_data(data)

def predict(train_data, test_data):
    columns_of_interest = ['close_26_ema','close_12_ema','macd','rsi_12',
                           'rsi_6','boll_ub','boll_lb','middle_20_sma','cci_20',
                           'middle_14_sma','cci_14','tr','atr','vr']
    train_x = np.array(train_data[columns_of_interest])
    test_x = np.array(test_data[columns_of_interest])

    
    t1_train = np.array(train_data['t1'])
    t2_train = np.array(train_data['t2'])
    t3_train = np.array(train_data['t3'])
    t4_train = np.array(train_data['t4'])
    t5_train = np.array(train_data['t5'])


    model = linear_model.Lasso(alpha=0.1)

    t1_fit = linear_model.LinearRegression().fit(train_x,t1_train)
    t2_fit = linear_model.LinearRegression().fit(train_x,t2_train)
    t3_fit = linear_model.LinearRegression().fit(train_x,t3_train)
    t4_fit = linear_model.LinearRegression().fit(train_x,t4_train)
    t5_fit = linear_model.LinearRegression().fit(train_x,t5_train)


    cci_14 = t1_fit.predict(test_x)
    cci_20 = t2_fit.predict(test_x)
    rsi_12 = t3_fit.predict(test_x)
    rsi_6 = t4_fit.predict(test_x)
    y = t5_fit.predict(test_x)
    return (cci_14,cci_20,rsi_12,rsi_6,y)

a,b,c,d,e = predict(train_data,test_data)
print(a,b,c,d,e)
    


