import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  striptest = test.replace(" ",'')
  # print striptest
  acc = 0
  for x in range(0, 16, 2):
  	acc += 2 * int(striptest[x])
  for x in range(1, 16, 2):
  	acc += int(striptest[x])
  # print acc
  if acc % 10 == 0:
  	print "Real"
  else:
  	print "Fake"

test_cases.close()
