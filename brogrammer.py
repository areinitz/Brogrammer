print "Welcome to Brogrammer"

ezR = 10
medR = 15
crayR = 20

ezS = 3
medS = 4
crayS = 5

work = raw_input("> ")

if work == "Arms" or work == "arms":
	print "Sun's out guns out, amirite?"
	print "OK, how hard are we going here, easy, medium, or CRAY?"

	effort = raw_input("> ")

	if effort == "easy" or effort == "Easy":
		print "Do %d sets of %d curls, %d sets of %d dips." % (ezS, ezR, ezS, ezR)
	elif effort == "medium" or effort == "Medium":
		print "Do %d sets of %d curls, %d sets of %d dips." % (medS, medR, medS, medR)
	elif effort == "CRAY" or effort == "cray":
		print "Get wild on %d sets of %d curls, %d sets of %d dips, and 50 pushups." % (crayS, crayR, crayS, crayR)
	else:
		print "%s sounds like a gnary typo, try again." % wo

print "OK good effort bro, get a shake."
