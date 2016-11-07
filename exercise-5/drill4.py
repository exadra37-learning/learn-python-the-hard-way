# Exercise 5
#
# Drill 4:
#   Try more format characters. %r is a very useful one. It's like saying "print this no matter what."

to_use_only_for_debug = "Print this with %r formatter, no matter what type of content it is. Use only for debug."
print "\n>>> print '%r' % to_use_only_for_debug"
print '%r' % to_use_only_for_debug


print "\n\n>>> Trying more Python Formatters as per https://pyformat.info <<<"

print """
---> Formatter Types Basics <---

Old Style Syntax:

    The place holder inside of a string to notify Python well a formatter will be declared is the symbol %, followed by
     a formatter type, like 'd', 's' or any other valid one.

    Syntax: %<formatter-type>

    Examples:
        - string formatter: %s
        - digit formatter: %d

New Style Syntax:

    The new syntax style swaps the use of place holder % with {} to notify Python where a formatter will be declared.

    Using default place holders {} for formatting will let Python handle the format types for us.

    We can also be more explicit and tell Python what we really want to format.

    Syntax: {<index>:<formatter-type>}

    Examples:
        - default: {}
        - default with indexx: {0}
        - string formatter: {:s}
        - digit formatter: {:d}
        - index with formatter type: {0:s}
"""

print "\n\n---> STRINGS"

print "\nOld Style Syntax:"

print "\n>>> print 'My nickname is %s and my true name is %s.' % ('Exadra37', 'Paulo Silva')"
print "My nickname is %s and my true name is %s." % ('Exadra37', 'Paulo Silva')


print "\n\nNew Style Syntax:"

print "\n>>> print 'My nickname is {:s} and my true name is {:s}.'.format('Exadra37', 'Paulo Silva')"
print "My nickname is {:s} and my true name is {:s}.".format('Exadra37', 'Paulo Silva')

print "\n>>> print 'My nickname is {} and my true name is {}.'.format('Exadra37', 'Paulo Silva')"
print "My nickname is {} and my true name is {}.".format('Exadra37', 'Paulo Silva')


print "\n\n---> NUMBERS"

print "\nOld Style Syntax:"

print "\n>>> print 'Learning Python in the Hard Way. Started in month %d of year %d.' % (10, 2016)"
print "Learning Python in the Hard Way. Started in month %d of year %d." % (10, 2016)

print "\n\nNew Style Syntax:"

print "\n>>> print 'Learning Python in the Hard Way. Started in month {:d} of year {:d}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in month {:d} of year {:d}.".format(10, 2016)

print "\n>>> print 'Learning Python in the Hard Way. Started in month {} of year {}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in month {} of year {}.".format(10, 2016)

print "\n>>> print 'Learning Python in the Hard Way. Started in year {1} on month {0}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in year {1} on month {0}.".format(10, 2016)

print "\n>>> print 'Learning Python in the Hard Way. Started in year {1:d} on month {0:d}.'.format(10, 2016)"
print "Learning Python in the Hard Way. Started in year {1:d} on month {0:d}.".format(10, 2016)


print "\n\n---> Aligning Strings <---\n"

print """
To align a string we need to specify the length of the string.

If the string provided to the formatter have less characters than the specified length than white spaces will be
used until the length is achieved.

So giving a string with 4 characters to a formatter that declares a string with a length of 10 characters, means that
when printing it on the screen, 6 white spaces will be allocated to the left or right side of the string, depending on
the type of alignment we have specify on the formatter, so that the total length will be 10 characters.

Old Style Syntax:
    By default it aligns to the right side of the string, therefore to align to right we don't need to specify the side
     we want to align, but we can do it if we want, as we will see on the examples.

    Syntax: %<side-to-align><string-length><formatter-type>

    Examples:
        - align to left(-) with length(10) using formatter(s): %-10s
        - align to right(+) with length(10) using formatter(s): %+10s

New Style Syntax:
    By default it aligns to left, the opposite side of Old Syntax.

    Also here we don't need to specify the side to align when we want to align to the left, but we can specify it if
     we want to be more explicit.

    Syntax: {:<side-to-align><string-length><formatter-type>}

    Examples:
        - align to left(<) with length(10) using formatter(s): {:<10s}
        - align to right(>) with length(10) using formatter(s): {:>10s}
"""

print "\n---> Align Right"

print "\nOld Style Syntax:"

print '\n>>> print "|%10s" % "test" * 2'
print "|%10s" % "test" * 2

print '\n>>> print "|%+10s" % "test" * 2'
print "|%+10s" % "test" * 2

print "\n\nNew Style Syntax:"

print "\n>>> print '|{:>10s}'.format('test') * 2"
print '|{:>10s}'.format('test') * 2

print "\n>>> print '|{:>10}'.format('test') * 2"
print '|{:>10}'.format('test') * 2

print "\n\n---> Align Left"

print "\nOld Style Syntax:"

print '\n>>> print "|%-10s" % "test" * 2'
print "|%-10s" % "test" * 2

print "\n\nNew Style Syntax:"

print "\n>>> print '|{:<10s}'.format('test') * 2"
print '|{:<10s}'.format('test') * 2

print "\n>>> print '|{:<10}'.format('test') * 2"
print '|{:<10}'.format('test') * 2

print "\n>>> print '|{:10}'.format('test') * 2"
print '|{:10}'.format('test') * 2


print "\n\n---> Padding Strings <---\n"

print """
Padding strings are not supported on Old style syntax.

Padding strings follows the same concept of Aligning strings, by allowing us to specify the character to put on the place of the white space.

Syntax: {:<padding_character><side-to-align><string-length><formatter-type>}

    Examples:
        - padding with character(_) on left side(<) with length(10) using formatter(s): {:_<10s}
        - padding with character(_) on right side(>) with length(10) using formatter(s): {:_>10s}
"""

print "\n---> Padding Left"

print "\nNew Style Syntax:"

print "\n>>> print '|{:_>10s}'.format('test') * 2"
print '|{:_>10s}'.format('test') * 2

print "\n>>> print '|{:_>10}'.format('test') * 2"
print '|{:_>10}'.format('test') * 2


print "\n\n---> Padding Right"

print "\nNew Style Syntax:"

print "\n>>> print '|{:_<10s}'.format('test') * 2"
print '|{:_<10s}'.format('test') * 2

print "\n>>> print '|{:_<10}'.format('test') * 2"
print '|{:_<10}'.format('test') * 2

print "\n>>> We only scratched the surface on Formatters. <<<\n"
