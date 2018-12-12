import sys
## Day 2 part 1


def RetreiveChksum(g):
	chksum_3, chksum_2 = 0,0
	gdic ={}
	for i in g:
		if i in gdic:
			get_count = gdic.get(i)
			gdic[i] = get_count+1
		else:
			gdic[i] = 1
	print gdic
	if 2 in gdic.values() and 3 in gdic.values():
		chksum_3 = 1
		chksum_2 = 1
		print 'yeay', g
	elif 2 in gdic.values() and 3 not in gdic.values():
		chksum_2 = 1
	elif 3 in gdic.values() and 2 not in gdic.values():
		chksum_3 = 1
	return[chksum_3, chksum_2]

FileIn = sys.argv[1]
chksum_2 = 0
chksum_3 = 0
with open(FileIn) as Finput:
	for line in Finput:
		LineParse = line.strip()
		out_temp=RetreiveChksum(g=LineParse)
		print out_temp
		chksum_3 += out_temp[0]
		chksum_2 += out_temp[1]
print 'CHECKSUM is {} '.format(chksum_2*chksum_3)

#Day 2 part 2

def RetreiveMatch(a, b):
	match = 0
	MisStr =''
	StrLength = len(a)
	assert len(a) == len(b)
	n =0
	StrMisIndex= 0
	for i, j in zip(a, b):
		n +=1
		if i == j:
			match += 1
		else:
			MisStr = i+'<>'+j
			StrMisIndex = n
	if match == StrLength-1:
		print ' STRING 1 {} \n STRING 2 {} \n MISMATCH AT {} {} \n THE INPUT TO PUZZLE IS {} '.format(a, b, MisStr, StrMisIndex, a[:StrMisIndex-1]+a[StrMisIndex:])
	

FileIn = sys.argv[2]
BoxID =[]
with open(FileIn) as InPut:
	for n, line in enumerate(InPut):
		LineParse= line.strip()
		BoxID.append(LineParse)
		for Id in BoxID:
			RetreiveMatch(Id, LineParse)
