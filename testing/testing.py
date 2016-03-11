import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  devstr, design = test.split(" | ")
  acc = 0
  for x, y in enumerate(devstr):
    if y != design[x]:
      acc += 1
  if acc == 0:
    print "Done"
  elif acc <= 2:
    print "Low"
  elif acc <= 4:
    print "Medium"
  elif acc <= 6:
    print "High"
  else:
    print "Critical"
test_cases.close()
