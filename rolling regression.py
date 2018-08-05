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

def transform_data(df):
    #
    #implement statistical inference with pvalues and rsquared to select features
    pass

def normalize_data(df):
    min_max_scaler = sklearn.preprocessing.MinMaxScaler()
    df['open'] = min_max_scaler.fit_transform(df.open.values.reshape(-1,1))
    df['high'] = min_max_scaler.fit_transform(df.high.values.reshape(-1,1))
    df['low'] = min_max_scaler.fit_transform(df.low.values.reshape(-1,1))
    df['close'] = min_max_scaler.fit_transform(df['close'].values.reshape(-1,1))
    return df

def choose_regressor(train_valid, test, models):
    columns_of_interest = ['Open','High','Low','Close']
    train_x = np.array(train_valid[columns_of_interest])
    train_y_high = np.array(train_valid['High_target'])
    train_y_low = np.array(train_valid['Low_target'])
    test_x = np.array(test[columns_of_interest])
    test_y_high = np.array(test['High_target'])
    test_y_low = np.array(test['Low_target'])

    high_scores = {}
    low_scores = {}
    model_dict = {'linear regression':linear_model.LinearRegression(copy_X=False, fit_intercept=True, n_jobs=1, normalize=False),
                   'ridge regression':linear_model.Ridge(alpha=0.5),
                   'lasso':linear_model.Lasso(alpha=0.1),
                   'bayesian ridge':linear_model.BayesianRidge()}
    
    model_names = ['linear regression','ridge regression','lasso','bayesian ridge']
    index = 0
    for model in models:
        high_fit = model.fit(train_x,train_y_high)
        low_fit = model.fit(train_x,train_y_low)
        high_scores[model_names[index]] = (high_fit.score(test_x,test_y_high))
        low_scores[model_names[index]] = (low_fit.score(test_x,test_y_low))
        index += 1
    high_scores_model = max(zip(high_scores.values(), high_scores.keys()))[1]
    low_scores_model = max(zip(low_scores.values(), low_scores.keys()))[1]  
    return model_dict[high_scores_model],model_dict[low_scores_model]

def training(train_data,high_scores_model,low_scores_model):
    columns_of_interest = ['Open','High','Low','Close']
    train_x = np.array(train_data[columns_of_interest])
    train_y_high = np.array(train_data['High_target'])
    train_y_low = np.array(train_data['Low_target'])
    high_fit = linear_model.LinearRegression().fit(train_x,train_y_high)
    low_fit = linear_model.LinearRegression().fit(train_x,train_y_low)
    return high_fit, low_fit
    

def get_predicted_prices(prediction_data,high_fit,low_fit):
    columns_of_interest = ['Open','High','Low','Close']
    prediction_points = np.array(prediction_data[columns_of_interest])
    print(prediction_points)
    predicted_high = high_fit.predict(prediction_points)
    predicted_low = low_fit.predict(prediction_points)
    return predicted_high, predicted_low

def plot_data():
    pass

models = [linear_model.LinearRegression(),linear_model.Ridge(alpha=0.5),
          linear_model.Lasso(alpha=0.1),linear_model.BayesianRidge()]


stock_symbol = 'AAPL'
train_valid_data = read_pickle(stock_symbol+"_train_valid_data.pkl")
test_data = read_pickle(stock_symbol+"_test_data.pkl")
train_data = read_pickle(stock_symbol+"_train_data.pkl")
prediction_data = read_pickle(stock_symbol+"_prediction_data.pkl")

high_scores_model, low_scores_model = choose_regressor(train_valid_data, test_data, models)
high_fit,low_fit = training(train_data, high_scores_model, low_scores_model)
next_day_high,next_day_low = get_predicted_prices(prediction_data, high_fit, low_fit)
print(next_day_high, next_day_low)
