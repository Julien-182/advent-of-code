
VARIATIONS = [int(line) for line in open("input")]

def partTwo():
	currentFreq = 0
	freqs={currentFreq}
	while True:
		for variation in VARIATIONS:
			currentFreq += variation
			if currentFreq in freqs:
				print(currentFreq)
				exit()
			else:
				freqs.add(currentFreq)	
			

partTwo()
