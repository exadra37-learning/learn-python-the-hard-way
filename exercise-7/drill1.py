# Exercise 7
#
# Drill 1:
#   Go back through and write a comment on what each line does.

# print to screen a string without any formatter
print "Mary had a little lamb."

# print to screen a string containing a string formatter, %s, that will be replaced by the string 'snow'.
print "Its fleece was white as %s." % 'snow'

# print to screen the string without any formatter
print "And everywhere that Mary went."

# print to screen the dot 10 times
print "." * 10 # what'd that do?

# assigning 1 letter to each variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# the comma in the end means no carriage return, therefore next print will place text on same line.
# all variables are concatenated, by using the + operator, to form the word Cheese
print end1 + end2 + end3 + end4 + end5 + end6,

# all variables are concatenated, by using the + operator, to form the word Burger
# this print start on same line of last one, therefore the final result is a string:
#   Cheese Burger
print end7 + end8 + end9 + end10 + end11 + end12
