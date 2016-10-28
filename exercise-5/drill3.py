print "Result of Searching Online for Python Format Characters"

print "\n*** My preference goes for this result: https://pyformat.info ***"

print "\n1. Basic Formatting:\n"

print "\n---> STRINGS <---\n"

# Old Style
print "Code (old strict approach):"
print ">>> print 'My nickname is %s and my true name is %s.' % ('Exadra37', 'Paulo Silva')"
print "My nickname is %s and my true name is %s." % ('Exadra37', 'Paulo Silva')
print "\n------\n"

# New Style
print "Code (new strict approach):"
print ">>> print 'My nickname is {:s} and my true name is {:s}.'.format('Exadra37', 'Paulo Silva')"
print "My nickname is {:s} and my true name is {:s}.".format('Exadra37', 'Paulo Silva')
print "\n------\n"

# New Style
print "Code (new non strict approach):"
print ">>> print 'My nickname is {} and my true name is {}.'.format('Exadra37', 'Paulo Silva')"
print "My nickname is {} and my true name is {}.".format('Exadra37', 'Paulo Silva')


print "\n\n---> NUMBERS <---\n"

# Old Style
print "Code (old strict approach):"
print ">>> print 'Learning Python in the Hard Way. Started in month %d of year %d.' % (10, 2016)"
print "Learning Python in the Hard Way. Started in month %d of year %d." % (10, 2016)

print "\n------\n"

print "Code (new strict approach):"
print ">>> print 'Learning Python in the Hard Way. Started in month {:d} of year {:d}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in month {:d} of year {:d}.".format(10, 2016)

print "\n------\n"

print "Code (new non strict approach):"
print ">>> print 'Learning Python in the Hard Way. Started in month {} of year {}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in month {} of year {}.".format(10, 2016)

print "\n------\n"

print "Code (new non strict approach):"
print "In this code example we will use place holders with the index position without specifying the format type."
print ">>> print 'Learning Python in the Hard Way. Started in year {1} on month {0}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in year {1} on month {0}.".format(10, 2016)

print "\n------\n"

print "Code (new strict approach):"
print "In this code example we will use place holders with the index position and strict format types."
print ">>> print 'Learning Python in the Hard Way. Started in year {1:d} on month {0:d}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in year {1:d} on month {0:d}.".format(10, 2016)

