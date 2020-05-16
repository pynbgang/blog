import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import basictools as bt
import pandas_datareader as pdr
import yfinance as yf
import os
import time
import optionsplay as op
import stockplay as sp
sns.set(style="whitegrid")
import stockplay as sp
str1='AMCR ,UAA ,RCL'
stocklist = str1.replace(" ","").split(",")
print op.caifuziyou(stocklist)

'''
output example
type list
stock name ,probablity to win ,profit ,strike ,how much to invest 
'''

print sp.caifuziyou(stocklist)

'''
output example
type list

['RCL', 38.029998779296875, 0.028999999999999998, 0.7623945220437599, 0]
 stock name,last day close price,probobility to increase, profit*8,how much need to invest 

'''
