import pandas as pd
import os
import queue
import time

directory = (__file__)
path = directory.replace(os.path.basename(__file__), 'Data\\')

data = pd.read_csv(path+'DASH.csv')


def list_manager(check_list: list, list_size: int):
	if len(check_list) > list_size:
		check_list.pop(0)
		list_manager(check_list, list_size)

count = []
for each in range(len(data['High'])):
	count.append(each)
cd = { #crypto_data
"Highs": data['High'],
"Lows": data['Low'],
"Open": data['Open'],
"Close": data['Close'],
"Count": count
}
for i in cd['Count']:
	#while cd['Count'][i+1] == True:
		try:
			if cd['Highs'][i] > cd['Highs'][i+1]:
				print(cd['Highs'][i])
		except:
			print("Done")




# for i in range(crypto_data["Count"]):
	# print(i)
	# print(crypto_data['Highs'])
	# print(crypto_data['Lows'][i])
	# print(crypto_data['Open'][i])
	# print(crypto_data['Close'][i])














'''
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
				print("")'''

















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