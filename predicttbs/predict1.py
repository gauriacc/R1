import pandas as pd
import numpy as np
import sys
import os
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from datetime import datetime
from datetime import timedelta
from datetime import date
#import ansible.runner


#inputs
input_file = "predictinp1.csv"
output_file = "output.csv"
#predict_file = sys.argv[1]
alert_ts = "/home/ansiblecontrol/tbs.log"
# alert_ts_props = alert_ts + "_props"

ds = pd.read_csv(input_file)
predict_file = "predict.csv"
out = pd.read_csv(output_file)
# out.head()
# ds.head()
#print(ds)
#print(ds.shape)

x = ds.iloc[:,:1]
y = ds.iloc[:,-1]
x_out = out.iloc[:,:1]
y_out = out.iloc[:,-1]
dts = ds.iloc[:,1]
#print(x)
#print(y)
#print(x_out)
#print(y_out)

#dat = ds['dates'].iloc[0]
#dat = ds['dts'].iloc[0]
first_date = ds.iloc[0,1]
#print(first_date)
#print(x_out)
#print(dat)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=1)
lr = LinearRegression()
lr.fit(x, y)
y_pred = lr.predict(x_out)
y_pred = y_pred.astype(int)
pred_day = y_pred[0]
print("Predicted number of days from start")
print(pred_day)

first_dates = datetime.strptime(first_date, "%d-%b-%y")
#print(first_dates)
first_dt = pd.to_datetime(first_dates).date()
#print(first_dt)
Begindate = datetime.strftime(first_dt, "%Y-%m-%d")
#print(Begindate)

target_date = first_dt + timedelta(days=int(pred_day))
print("Target dates is") 
print(target_date)
today = date.today()
#print(today)
day_pending = target_date - today
#print(day_pending)
days1 = day_pending.days
print("number of days from current date")
print(days1)
if days1 <= 10:
   color_format = "red"
   warn_ts = True
   action = "Extend Table space database"
   print(warn_ts)
   actionColor = "green"
else:
    color_format = "tblColor"
    action = "No Action Needed"

if warn_ts:
    with open(alert_ts, 'w') as fp:
        fp.write("extend_ts")
    fp.close()
