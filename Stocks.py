from yahoo_fin.stock_info import *
from pandas import *
import os
import sys
import math


chosen_stocks = [] #Stores tickers of stocks I choose
volume_stocks = [] #Volume of the tickers I choose
potential_stocks = get_day_gainers() 

#This functions purpose is to get the top 100 stocks and narrow the list
#Down to stocks that's abbreviation is 4 characters or less because I don't
#Like to trade 5 character long stocks(I find they tend to be unreliable)
#This function ALSO  is to get the volume correlating to the right stock tickers
#I want only stocks with at least 5m in volume
def getNames():
    stock_names = potential_stocks[potential_stocks.columns[0]]
    stock_volume = potential_stocks[potential_stocks.columns[5]]
    
    i = 0
    for x in stock_names:
        volume = round(stock_volume[i])
        if len(x) < 5:      
            #if volume < :#More than 1m volume
                if volume > 500000:#More than 500k volume
                    chosen_stocks.append(x)
                    volume_stocks.append(stock_volume[i])
                    
        i = i + 1

#This will eventually get changed to username and password to sign
#Into a brokage account
try:
    with open(os.path.join(sys.path[0],"DollarAmt.txt"), "r") as Amt:
        dollar = Amt.read()
except:
    print("File DollarAmt.txt not found. Check your path and try again")
    sys.exit()

#potential_stocks = get_day_gainers()
#print(potential_stocks)


getNames()#Global Variables are being changed

i = 0
for x in volume_stocks:
    print(chosen_stocks[i])
    print(volume_stocks[i])
    i = i + 1

Amt.close()#This is the text file for dollar amount in acc
