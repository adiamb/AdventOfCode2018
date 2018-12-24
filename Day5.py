import sys
import re
from operator import itemgetter
key = itemgetter(1)

## PART 1
def ParseStr(StrIn):
	Strout=['']
	for i in StrIn:
		if i == Strout[-1].swapcase():
			Strout.pop()
		else:
			Strout.append(i)
	return ''.join(Strout)
  
FileIn = open(sys.argv[1])
StrIn = FileIn.readline()
len(ParseStr(StrIn= StrIn.strip()))

## PART2
FileIn = open(sys.argv[1])
StrIn = FileIn.readline()
Strout={}
StrIn=StrIn.strip()
for i in StrIn.strip():
	K = i.lower()
	if K not in Strout:
		MakeString = re.sub(K, '', StrIn, flags=re.IGNORECASE)
		ParseString = len(ParseStr(MakeString))
		Strout[K] = ParseString
min(Strout.items(), key=key)
