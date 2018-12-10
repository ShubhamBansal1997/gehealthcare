from gehealthcare.labevents.models import Labevent, Item
from gehealthcare.users.models import User
from datetime import datetime
import csv
import pytz
import dateutil.parser

with open('LABEVENTS.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	tz = pytz.timezone('Asia/Kolkata')
	count = 0
	for row in csv_reader:
		if row[0] != '':

			if count != 0:
				# if row[1] != '':
				# 	startdate = datetime.strptime(row[1], '%Y-%m-%d').date()
				# 	print(startdate)
				# 	startdate = startdate.replace(year=2016)
				# 	print(startdate)
				# else:
				# 	startdate = ''
				# if row[2] != '':
				# 	enddate = datetime.strptime(row[2], '%Y-%m-%d')
				# 	enddate = datetime.replace(year=2016)
				# else:
				# 	enddate = ''
				item = None
				try:
					item = Item.objects.get(item_id=row[1])
				except:
					item = None
				if row[1] != '':
					charttime = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
					charttime = charttime.replace(year=2016, tzinfo=tz).isoformat()
					#print(admittime)
				else:
					admittime = ''
				try:
					user = User.objects.get(hadm_id=row[0])
					if item != None:
						print(row)
						labevent = Labevent(
							user=user,
							hadm_id=row[0],
							item=item,
							item_data_id=row[1],
							charttime=dateutil.parser.parse(charttime),
							value=row[3],
							valueom=row[4],
							flag=row[5]
						)
						labevent.save()
				except:
					if item != None:
						print(row)
						labevent = Labevent(
							hadm_id=row[0],
							item=item,
							item_data_id=row[1],
							charttime=dateutil.parser.parse(charttime),
							value=row[3],
							valueom=row[4],
							flag=row[5]
						)
						labevent.save()

				#print(startdate)
				#print(enddate)
				


			count = count + 1