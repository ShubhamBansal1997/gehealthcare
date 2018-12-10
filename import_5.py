from gehealthcare.diagnoses.models import IcCode

lines = [line.rstrip('\n') for line in open('ic9codes.txt')]
for line in lines:
	line = line.strip()
	line = line.split(',')
	for word in line:
		word = word.strip()
		word = word.split(':')
		if len(word) >= 2:
			item = IcCode(
				ic_id=word[0].strip()[1:-1],
				ic_name=word[1].strip()[1:-1]
			)
			item.save()
			print("break")
		else:
			print("lol")