from gehealthcare.diagnoses.models import IcCode, Diagnoses
from gehealthcare.users.models import User
from datetime import datetime
import csv
import pytz
import dateutil.parser

with open('DIAGNOSES_ICD.csv') as csv_file:
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
					item = IcCode.objects.get(ic_id=row[2])
				except:
					item = None
				try:
					user = User.objects.get(hadm_id=row[0])
					if item != None:
						print(row)
						labevent = Diagnoses(
							user=user,
							hadm_id=row[0],
							seq_num=int(row[1]),
							ic=item,
							ic_data_id=row[2]
						)
						labevent.save()
				except:
					if item != None:
						print(row)
						labevent = Diagnoses(
							hadm_id=row[0],
							seq_num=int(row[1]),
							ic=item,
							ic_data_id=row[2]
						)
						labevent.save()

				#print(startdate)
				#print(enddate)
				


			count = count + 1