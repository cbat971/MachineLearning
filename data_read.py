import pandas as pd
import os
import queue
import time

directory = (__file__)
path = directory.replace(os.path.basename(__file__), 'Data\\')

data = pd.read_csv(path+'DASH.csv')
print(data)

def list_manager(check_list: list, list_size: int):
	if len(check_list) > list_size:
		check_list.pop(0)
		list_manager(check_list, list_size)


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
	list_of_highs.append(highs)
	# list_manager(list_of_highs, 5)
	# print(list_of_highs)
	# time.sleep(.1)



differences = []

print(list_of_highs)

for idx, val in enumerate(reversed(list_of_highs)):
	if idx < 500:
		if data['High'][int(idx+1)]-data['Low'][int(idx)] > .00001:
			percent_change = (data['High'][int(idx+1)]-data['Low'][int(idx)])/data['High'][int(idx+1)]
			if percent_change > .01:
				print("The low was: ")
				print(data['Low'][int(idx)])
				print("The high was: ")
				print(data['High'][int(idx+1)])
				print("The difference in satoshi's is: ")
				print(percent_change)
				print("")
				print("")

















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