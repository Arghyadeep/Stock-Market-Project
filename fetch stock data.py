#dependencies
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()

def get_stock_data(symbol,start,end):
    #implement exception handling for symbol and dates
    data = pdr.get_data_yahoo(symbol,start,end)
    return data


def save_data(filename,data):
    #implement exception handling for path
    path = "data/"+filename+".csv"
    data.to_csv(path)

symbol = 'AAPL'
start = '2010-01-01' #set this to get 10 years data wrt to current date
end = '2018-05-30'  #use datetime to get today's date

data = get_stock_data(symbol,start,end)
save_data(symbol,data)
#print(data.tail(2))
#print(data.head(2))
#print(len(data))
                                        
    
