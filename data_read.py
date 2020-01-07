import pandas as pd
import os
import queue

directory = (__file__)
path = directory.replace(os.path.basename(__file__), 'Data\\')

data = pd.read_csv(path+'DASH.csv')
print(data)


list_of_lows = []
list_of_highs = []
list_of_open = []
list_of_close = []
L = queue.Queue(maxsize=20)
L.put(5)
L.put(9)
L.put(1)
L.put(7)
print(L.get())
print(L.get())
print(L.get())
print(L.get())
A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=Z = ''
for highs in data['High']:
	print(highs)















"""import os
import pandas as pd
import datetime
import csv"""

"""directory = (__file__)
path = directory.replace(os.path.basename(__file__), 'Data\\')
count_list = []
data = pd.read_csv(path+"DASH.csv")
df = pd.DataFrame(data)
# print(data.head())
# print(data.shape)
# print(data.describe())
for dates in data["Date"]:
	# print((dates))
	date_time_obj = datetime.datetime.strptime(dates, '%Y-%m-%d %I-%p')
	print(type(date_time_obj))
	

"""