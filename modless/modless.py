import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	quotient, divisor = map(int, test.split(','))

	print quotient - divisor * (quotient/divisor)        
test_cases.close()
