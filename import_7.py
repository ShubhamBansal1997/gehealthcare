from gehealthcare.users.models import User
import csv

with open('district_disease_data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	count = 0
	for row in csv_reader:
		if count != 0:

			try:
				user = User.objects.get(hadm_id=row[0])
				user.state = row[2]
				user.district = row[3]
				user.save()
			except:
				print("fucked")
		count = count + 1
