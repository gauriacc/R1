import pandas as pd
import numpy as np
import sys
import os
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
#import ansible.runner
import time


#inputs
df = pd.read_csv('predictinp.csv')
df['dt'] = pd.to_datetime(df.dt, format="%d-%b-%Y")
#df['date'] = data_df['Date'].map(dt.datetime.toordinal)
df['dt'] = df['dt'].apply(lambda  var: time.mktime(var.timetuple()))
X = df[['dt']]
y = df['used']
