import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  # split into country groups
  countries = test.strip("\n").split(" | ")
  # split teams
  countries = [x.split() for x in countries]

  #hash teams
  teams = {} 
  for y, x in enumerate(countries):
  	for z in x:
  		if not z in teams.keys():
  			teams[z] = [y+1]
  		else:
  			teams[z].append(y+1)
  for x in map(str,sorted(map(int,teams.keys()))):
  	sys.stdout.write(x + ":")
  	for y, z  in enumerate(teams[x]):
  		if y < len(teams[str(x)]) - 1 :
  			sys.stdout.write(str(z) + ",")
  		else:
  			sys.stdout.write(str(z) + "; ")
  print

test_cases.close()
