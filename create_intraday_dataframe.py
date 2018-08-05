import pandas as pd
from pandas import datetime
import numpy as np
import pickle as pkl
#from statsmodels.tsa.arima_model import ARIMA

def fetch_data(filename):
    path = "data/"+filename
    data = pd.read_csv(path)
    print(data.tail())
    return data

def get_values(data):
    Open = list(data['Open'])
    Close = list(data['Close'])
    High = list(data['High'])
    Low = list(data['Low'])
    return Open, High, Low, Close

def create_dataframe(data):
    Open, High, Low, Close = get_values(data)
    columns = ['Open','High','Low','Close','Low_target','High_target']
    High_target = High
    Low_target = Low
    High_target.remove(High_target[0])
    Low_target.remove(Low_target[0])
    High_target.append(0)
    Low_target.append(0)
    df = data
    df['High_target'] = High_target
    df['Low_target'] = Low_target
    df.drop('Volume', axis = 1, inplace = True)
    df.drop('Adj Close',  axis = 1, inplace= True)
    return df

def train_test_split(data, split):
    train_valid_size = int(len(data)*split)
    train_valid = data[:train_valid_size]
    test = data[train_valid_size+1:len(data)-2]
    train = data[:len(data)-1]
    prediction = data[len(data)-1:]
    return train_valid,train,test,prediction


def dump_pickle(obj, pickle_name):
    path = "pickles/"
    if not type(obj) == type(pd.DataFrame()):
        raise TypeError("object to dump must be DataFrame")
    pkl.dump(obj, open(path+pickle_name, "wb"))

filename = "AAPL.csv"
data = fetch_data(filename)
df = create_dataframe(data)
train_valid, train, test, prediction = train_test_split(df,0.8)
print(train_valid.head())
#print(train.head())
#print(test.head())
#print(prediction.head())
dump_pickle(train_valid, filename[:-4] + "_train_valid_data.pkl")
dump_pickle(train, filename[:-4] + "_train_data.pkl")
dump_pickle(test, filename[:-4] + "_test_data.pkl")
dump_pickle(prediction, filename[:-4] + "_prediction_data.pkl")
