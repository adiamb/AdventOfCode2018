import sys
##Day3 Part 1
## A generic Functin to process the claimID and return coords
def ProcessClaim(Claim):
	ClaimParse=Claim.split(' ')
	assert len(ClaimParse) == 4
	ClaimID = ClaimParse[0]
	Xoff = int(ClaimParse[2].split(',')[0])
	Yoff = int(ClaimParse[2].split(',')[1].replace(':',''))
	Width = int(ClaimParse[-1].split('x')[0])
	Height = int(ClaimParse[-1].split('x')[1])
	#Coord1 = str(Xoff)+ ','+str(Yoff)
	#Coord2 = str(Xoff+Width)+ ','+str(Yoff+Height)
	RowCoords=[i for i in range(Xoff, Xoff+Width)]
	ColCoords=[i for i in range(Yoff, Yoff+Height)]
	OutCoords = []
	AreaCount = 0
	for i in RowCoords:
		for j in ColCoords:
			OutCoords.append(str(i)+','+str(j))
			AreaCount += 1
	assert AreaCount == Width*Height
	return OutCoords
	
### find the overlap by filling up a dictionary
TrackDic ={}
FileIn = sys.argv[1]
Claims =[]
with open(FileIn) as InPut:
	for line in InPut:
		if line:
			Claim = line.strip()
			ClaimID=Claim.split(' ')[0]
			if ClaimID not in Claims:
				Claims.append(ClaimID)
			MarkCoords = ProcessClaim(Claim = Claim)
			for key in MarkCoords:
				if key in TrackDic:
					#overlap += 1
					get_claim = TrackDic.get(key)
					TrackDic[key] = get_claim + '$' +ClaimID
				else:
					TrackDic[key] = ClaimID

### count how many claims each coordinate takes up
overlap = 0
for k, v in TrackDic.items():
	if len(v.split('$')) > 1:
		overlap += 1
print 'Total sq inches that are overalapped are {} '.format(overlap)

## Get nonoverlapping claims
for claim in Claims:
	if claim not in overlaplist:
		print 'CLAIMS THAT DONT OVERLAP ARE {}'.format(claim)
