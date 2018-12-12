import sys
## Part 1
FileIn = sys.argv[1]
CurFreq =0
with open(FileIn) as FreqIn:
	for line in FreqIn:
		FreqAdju = int(line.strip())
		CurFreq += FreqAdju
print CurFreq

## Part 2
FileIn = sys.argv[2]
CurFreq =0
FreqDic ={}
ReadFile = True
while ReadFile is True:
	with open(FileIn) as FreqIn:
		for line in FreqIn:
			FreqAdju = int(line.strip())
			if CurFreq not in FreqDic:
				FreqDic[CurFreq] =0
				CurFreq += FreqAdju
			else:
				print CurFreq
				ReadFile =False
				break
