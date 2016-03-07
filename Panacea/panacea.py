import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	# Split on pipeline
	testArr = test.split(' | ')
	virusSum = sum(int(x, 16) for x in testArr[0].split())
	antivirusSum = sum(int(x, 2) for x in testArr[1].split())
	print virusSum <= antivirusSum
test_cases.close()