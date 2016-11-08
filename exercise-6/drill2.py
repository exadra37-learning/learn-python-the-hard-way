# Exercise 6
#
# Drill 2:
#  Find all the places where a string is put inside another string. There are four places.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# 2 strings inside another string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# 1 String inside another string
print "I said: %r." % x

# 1 String inside another string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
