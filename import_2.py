from gehealthcare.prescriptions.models import Prescription
from gehealthcare.users.models import User
from datetime import datetime
import csv
import pytz
import dateutil.parser

with open('PRESCRIPTIONS.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	tz = pytz.timezone('Asia/Kolkata')
	count = 0
	for row in csv_reader:
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
			startdate = "2016"+row[1][4:]
			enddate = "2016"+row[2][4:]
			try:
				user = User.objects.get(hadm_id=row[0])
				prescription = Prescription(
					user=user,
					hadm_id=row[0],
					startdate=dateutil.parser.parse(startdate),
					enddate=dateutil.parser.parse(enddate),
					drug=row[3],
					drug_name=row[4],
					webmd_link=row[5],
					prod_strength=row[6],
					dose_val=row[7],
					dose_unit=row[8]
				)
				prescription.save()
			except:
				print(row[0])
				prescription = Prescription(
					hadm_id=row[0],
					startdate=dateutil.parser.parse(startdate),
					enddate=dateutil.parser.parse(enddate),
					drug=row[3],
					drug_name=row[4],
					webmd_link=row[5],
					prod_strength=row[6],
					dose_val=row[7],
					dose_unit=row[8]
				)
				prescription.save()

			#print(startdate)
			#print(enddate)
			


		count = count + 1