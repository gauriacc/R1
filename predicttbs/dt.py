import pandas as pd
from datetime import datetime
from datetime import timedelta
first = "03-08-2023"
Begindate = datetime.strptime(first, "%d-%m-%Y")
print(Begindate)
day = 10
enddate = Begindate + timedelta(days=day)
#next = pd.to_datetime(enddate).date()
next = enddate.date()
print(next)
from datetime import date
today = date.today()
print("Today date is: ", today)

