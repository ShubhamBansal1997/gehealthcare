from gehealthcare.labevents.models import Item

lines = [line.rstrip('\n') for line in open('itemid.txt')]
for line in lines:
	line = line.strip()
	line = line.split(',')
	for word in line:
		word = word.strip()
		word = word.split(':')
		if len(word) >= 2:
			item = Item(
				item_id=word[0].strip()[1:-1],
				item_name=word[1].strip()[1:-1]
			)
			item.save()
			print("break")
		else:
			print("lol")