import sys
test_cases = open(sys.argv[1], 'r')

def compCardVal(hand1, hand2):
	# 
	hand1Arr = list(hand1)
	hand2Arr = list(hand2)

	# check for 10 and correct
	def correct10(hand):
		if len(hand) > 2:
			return ['10', hand[-1]]
		else:
			return hand

	hand1Arr = correct10(hand1Arr)
	hand2Arr = correct10(hand2Arr)

	# card value to number
	def valToNum(hand):
		if hand[0] == 'A':
			return [14, hand[-1]]
		elif hand[0] == 'K':
			return [13, hand[-1]]
		elif hand[0] == 'Q':
			return [12, hand[-1]]
		elif hand[0] == 'J':
			return [11, hand[-1]]
		else:
			return [int(hand[0]), hand[1]]

	hand1Arr = valToNum(hand1Arr)
	hand2Arr = valToNum(hand2Arr)

	# compare values

	if hand1Arr[0] > hand2Arr[0]:
		print hand1
	elif hand1Arr[0] < hand2Arr[0]:
		print hand2
	else:
		print hand1 + " " + hand2


for test in test_cases:
	testArr = test.split(' | ')
	trump = testArr[1][0]
	hand1 = testArr[0].split()[0]
	hand2 = testArr[0].split()[1]

	# check trump first
	if hand1[-1] == trump and hand2[-1] == trump:
		# compare on value
		compCardVal(hand1, hand2)
	elif hand1[-1] == trump:
		print hand1
	elif hand2[-1] == trump:
		print hand2
	else:
		# compare on value
		compCardVal(hand1, hand2)

test_cases.close()
