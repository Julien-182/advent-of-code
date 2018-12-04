
IDS = [line for line in open("input")]

def partOne():
	twoLetters=set()
	threeLetters=set()

	for id in IDS:
		for letter in set(id):
			if id.count(letter) == 2:
				twoLetters.add(id)
			elif id.count(letter) == 3:
				threeLetters.add(id)

	print(len(twoLetters) * len(threeLetters))


def partTwo():
	
	for id in IDS:
		for idCompare in IDS:
			if id != idCompare:
				if getDifferences(id,idCompare) == 1:
					print(id)
					print(idCompare)
					return
	 

def getDifferences(string1,string2):
	difference=0
	for i in range(len(string1)):
		if string1[i-1] != string2[i-1]:
			difference+=1
	return difference
		

partOne()
partTwo()
