---
layout: post
title: "option trading"
published: true
created:  2020 Apr 23 01:09:58 PM
tags: [python, project]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# owen
# new updated is under /optiontrading

studing on basic knowledge of pandas,yfinace,matplotlib.

```python
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.dates as dates
data1 = yf.download('AAPL','2015-01-13','2020-04-20')
data2 = yf.download('oxy','2020-01-13','2020-04-20')
x1=np.array(data1.index)
y=np.array([i for i in data1['Close']])
x2=np.array(data2.index)
z=np.array([i for i in data2['Close']])
fig,axes=plt.subplots(1,2,figsize=(15,15))
axes[0].plot_date(x1,y,"-")
axes[0].yaxis.grid(True)
axes[1].plot_date(x2,z,"-")
fig.autofmt_xdate()
plt.show()

---phase 1
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
def get_stock_data(start_time,end_time,*stocklist):
    if not stocklist:return {}
    data_dict={}
    for i  in stocklist:
        data1 = yf.download(i,start_time,end_time)
        data_dict[i]=data1
    return data_dict

if __name__ == "__main__":
    pass
    
----phase 2

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime
import os
import pandas_datareader as pdr

def get_stock_data(start_time,end_time,*stocklist):
    if not stocklist:return {}
    data_dict={}
    days = [10, 20, 50]
    for i  in stocklist:
        try:
            data1 = yf.download(i,start_time,end_time)
            for day in days:
                columnday = str(day) + " days"
                data1[columnday] = data1['Adj Close'].rolling(day).mean()
            data_dict[i]=data1[["Adj Close","10 days","20 days","50 days"]]
        except:pass
    return data_dict

def get_next_event(*stocklist):
    if not stocklist: return {}
    data_next_ear_data={}
    for i in stocklist:
        try:
            temp = yf.Ticker(i)
            templist=temp.calendar.loc['Earnings Date'].tolist()
            if templist:
                data_next_ear_data[i]=str(templist[0])[0:10]
        except:pass
    return data_next_ear_data

def get_data(days):
    cur=datetime.date.today()
    delta=datetime.timedelta(days=days)
    return str(cur-delta)

def get_date_delta(str1,str2):
    date_time_obj1 = datetime.datetime.strptime(str1, '%Y-%m-%d')
    date_time_obj2 = datetime.datetime.strptime(str2, '%Y-%m-%d')
    l=str(date_time_obj1-date_time_obj2).split()
    if "days," in l:return int(l[0])
    else:return 0

def get_options_data(date_str,cp="call",*stocklist):
    if not stocklist: return {}
    data_options={}
    for i in stocklist:
        try:
            temp=yf.Ticker(i)
            if cp=="put":data_options[i]=temp.option_chain(date_str).puts
            else:data_options[i]=temp.option_chain(date_str).calls
        except:pass
    return data_options

def mail_notice(msg,*maillist):
    for i in maillist:
        try:
            str1 ="sudo echo " + "\'"+msg+" "+" \'" +"| "+"mail -s " +"\'" + "less then 20 days left to earning call" + "\' " +i
            os.system(str1)
        except:pass
    return


def perdict10days(startprice,mu,dt,sigma,days=10):
    price=np.zeros(days)
    price[0]=startprice
    shock=np.zeros(days)
    drift=np.zeros(days)
    for x in range(1,days):
        shock[x]=np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        drift[x]=mu*dt
        price[x]=price[x-1]+(price[x-1]*(drift[x]+shock[x]))
    return price

#def kelly_caculation():
    #return invest_percentage

if __name__ == "__main__":
    pass

```

# Kelly Criterion 
- https://www.investopedia.com/articles/trading/04/091504.asp
- https://zhuanlan.zhihu.com/p/21084686


