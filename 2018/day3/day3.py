
EMPTY='.'
OVERLAP='X'
FABRIC = [[EMPTY for j in range(1000)] for i in range(1000)]
CLAIMS = [line for line in open("input")]

def partOne():
	for claim in CLAIMS:
		data = parseLine(claim)
		drawSquare(data[0],data[1],data[2],data[3],data[4])		
	
	print(countOverlap())	

def parseLine(line):
	tmp = line.replace(" @","").replace('#','').split(' ')
	id = tmp[0]	
	offsetX = int(tmp[1].split(',')[0])
	offsetY = int(tmp[1].split(',')[1].replace(':',''))
	sizeX = int(tmp[2].split('x')[0])
	sizeY = int(tmp[2].split('x')[1])
	return id,offsetX,offsetY,sizeX,sizeY

def drawSquare(id, offsetX, offsetY, sizeX, sizeY):
	for y in range(offsetY, offsetY+sizeY):
		for x in range(offsetX, offsetX+sizeX):
			if FABRIC[x][y] == EMPTY:
				FABRIC[x][y] = id
			else:
				FABRIC[x][y] = OVERLAP
		
def countOverlap():
	cpt = 0
	for i in range(1000):
		for j in range(1000):
			if FABRIC[i-1][j-1] == OVERLAP:
				cpt += 1		
	return cpt


def partTwo():
	for claim in CLAIMS:
		data = parseLine(claim)
		if isSquareIntact(data[0],data[1],data[2],data[3],data[4]):
			print(data[0])
			return		
	
def isSquareIntact(id, offsetX, offsetY, sizeX, sizeY):
	for y in range(offsetY, offsetY+sizeY):
		for x in range(offsetX, offsetX+sizeX):
			if FABRIC[x][y] != id:
				return False
	return True

##################################

partOne()
partTwo()
