import datetime
from time import strftime
now=datetime.datetime.now()
print(strftime("%d/%m/%y"))
print(datetime.date.today().month)
x=datetime.datetime(year=2020,day=4,month=12)
y=datetime.datetime(year=2020,day=3,month=12)
dif=x-y
print(dif)
end=datetime.datetime.now()
difference=end-now
print(x)
print(difference)