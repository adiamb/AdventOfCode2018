from collections import defaultdict
import sys
import re
from operator import itemgetter
FileIn = sys.argv[1]
MasterTrack = [line.strip() for line in open(FileIn) if line]
Guard = defaultdict(int)
TimeTrack = defaultdict(lambda:defaultdict(int))
#b = '[1518-03-03 00:00] Guard #3181 begins shift'
GuardRe = '(?<=#)\d+'
MinRe = '(?<=:)\d+'
CurGuard = None
for item in sorted(MasterTrack):
	print item
	if 'Guard' in item:
		GuardM = re.search(GuardRe, item)
		GuardId = int(GuardM.group(0))
		CurGuard = GuardId
	elif 'asleep' in item:
		MinAsleep = re.search(MinRe, item)
		MinInt = int(MinAsleep.group(0))
	elif 'wakes' in item:
		MaxAsleep = re.search(MinRe, item)
		MaxInt = int(MaxAsleep.group(0))
		assert MinInt < MaxInt
		for i in xrange(MinInt, MaxInt):
			Guard[CurGuard] += 1
			TimeTrack[CurGuard][i] += 1
## PART 1
key = itemgetter(1) # compare the value in the (key, value) pairs
GMax = max(Guard.items(), key=key)[0]
GMaxMin = max(TimeTrack[GMax].items(), key=key)[0]
print(GMax * GMaxMin)