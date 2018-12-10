from gehealthcare.users.models import User
from datetime import datetime
import csv
import pytz
import dateutil.parser


with open('Admission.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	tz = pytz.timezone('Asia/Kolkata')
	count = 0
	for row in csv_reader:
		if count != 0:
			if row[1] != '':
				admittime = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
				admittime = admittime.replace(year=2016, tzinfo=tz).isoformat()
				#print(admittime)
			else:
				admittime = ''
			if row[2] != '':
				dischtime = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
				dischtime = dischtime.replace(year=2016, tzinfo=tz).isoformat()
			else:
				dischtime = ''
			if row[3] != '':
				deathtime = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
				deathtime = deathtime.replace(year=2016, tzinfo=tz).isoformat()

			else:
				deathtime = ''
			user = User(
				first_name='Anonymous',
				email='Anonymous{}@gmail.com'.format(row[0]),
				hadm_id=row[0],
				admittime=dateutil.parser.parse(admittime),
				dischtime=dateutil.parser.parse(dischtime),
				deathtime=dateutil.parser.parse(admittime),
				admission_type=row[4],
				admission_location=row[5],
				discharge_location=row[6],
				insurance=row[7],
				language=row[8],
				religion=row[9],
				martial_status=row[10],
				ethnicity=row[11],
				diagnosis=row[12]
				)

			user.save()
		count = count + 1