#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
from datetime import date, timedelta
import serial


# In[2]:


watchlist = ['TSLA','FCEL', 'IDEX','PLUG','HIMX']

today = date.today()
      
def get_current_price():
    global prices
    prices=[]    
    for i in watchlist:  
        data = yf.download(tickers=i, period='5m', interval='5m')
        price=(round(((data['Close'][0])),2))
        prices.append('$'+str(price))
    return(prices)

def get_current_percentage():
    global percentages
    percentages=[]    
    for j in watchlist:
        stock = yf.Ticker(j)
        if (date.today().weekday()) == 0:
            yesterday = date.today()-timedelta(3)
        if (date.today().weekday()) > 0:
            yesterday = date.today()-timedelta(1)
        last_close = stock.history(start=yesterday, end=today)['Close'][0]
        data = yf.download(tickers=j, period='5m', interval='5m')
        price = data['Close'][0]
        raw_percent = price/last_close
        if raw_percent>1:
            real_percent = round(((raw_percent-1)*100),2)
        if raw_percent<=1:
            real_percent = (round(((1-raw_percent)*100),2))*-1
        percentages.append(str(real_percent) + '%')
    
    return(percentages)

def display():
    get_current_price()
    get_current_percentage()
    info=[]
    for k in range(len(watchlist)):
        info.append(watchlist[k])
        info.append(prices[k])
        info.append(percentages[k])
    return(info)
        
print(display())
        


# In[ ]:




