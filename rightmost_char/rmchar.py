import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	field, finder = test.strip("\n").split(',')
	try:
		print len(field) - field[::-1].index(finder) -1
	except Exception, e:
		print -1

test_cases.close()