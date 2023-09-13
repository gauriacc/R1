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
sys.path.append(os.environ['WORKSPACE'])


#inputs
input_file = predictinp1.csv
output_file = output.csv
#predict_file = sys.argv[1]
#alert_ts = sys.argv[2]
# alert_ts_props = alert_ts + "_props"

ds = pd.read_csv(input_file)
predict_file = "predict.csv"
out = pd.read_csv(predict_file)
# out.head()
# ds.head()
#print(ds)
#print(ds.shape)

x = ds.iloc[:,:-1]
y = ds.iloc[:,1]
x_out = out.iloc[:,:-1]
y_out = out.iloc[:,1]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=1)
#print(X_train.shape)
#print(X_test.shape)
#print(y_train.shape)
#print(y_test.shape)

lr = LinearRegression()
lr.fit(x, y)

#print(lr.intercept_)
#print(lr.coef_)
#print(X_train.shape)
y_pred = lr.predict(x_out)
warn_ts = False
if y_pred <= 10:
   color_format = "red"
   warn_ts = True
   action = "Extend Table space database"
   actionColor = "green"
else:
    color_format = "tblColor"
    action = "No Action Needed"

wl = x_out
space = y_pred
if warn_ts:
    with open(alert_ts, 'w') as fp:
        fp.write("extend_ts")
    fp.close()
    

wl['space'] = space

result = wl.to_csv("output.csv", header=True, index=False)
#sno += 1

if not os.path.isfile(alert_ts):
    with open(alert_ts, 'w') as fp:
        fp.write('no_action_needed')    
        fp.close()

#print(y_out,y_pred)
#print("Mean squared error is: ",mean_squared_error(y_test,y_pred))
df = pd.DataFrame({'Actual': y_out, 'Predicted': y_pred})
print(df)
#print(y_pred)
#comparison_df = pd.DataFrame({"Actual":y_test,"Predicted":y_pred})
#print(comparison_df)
#plt.scatter(X_train, y_train, color = "red")
#plt.plot(X_test, y_pred, color='green')
# Adding title and labels
#plt.xlabel("Workload") # adding the X-axis label
#plt.ylabel("Space") # adding the Y-axis label
#plt.title("This is the title of of the plot") # adding the title

# Displaying the line chart
#plt.show()

