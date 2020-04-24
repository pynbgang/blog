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

# owen studing on basic knowledge of pandas,yfinace,matplotlib.

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
```

# Kelly Criterion 
These two factors are then put into Kelly's equation which is:

\begin{aligned} & K\% = W - \frac{\left(1-W\right )}{R}\\ \textbf{where:}\\ &K\% = \text{The Kelly percentage}\\ &W = \text{Winning probability}\\ &R = \text{Win/loss ratio}\\ \end{aligned} 
where:
​	  
K%=W− 
R
(1−W)
​	 
K%=The Kelly percentage
W=Winning probability
R=Win/loss ratio
​	https://zhuanlan.zhihu.com/p/21084686

