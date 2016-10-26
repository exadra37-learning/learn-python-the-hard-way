# where are my chickens???
print "I will now count my chickens:"

# maths sequence:
#   30 / 6 = 5
#   25 + 5 = 30
print "Hens", 25 + 30 / 6

# maths sequence:
#   25 * 3 = 75
#   75 % 4 = 3
#   100 - 3 = 97
#print (100 - ((25 * 3) % 4))
print "Roosters", 100 - 25 * 3 % 4

# Hopping to not break any egg...
print "Now I will count the eggs:"

# maths sequence:
#   3 + 2 + 1 = 6
#   6 - 5 = 1
#
#   4 % 2 = 0
#   1 / 4 = 0
#   0 + 6 = 6
#   0 - 6 = 6
#
#   1 + 6 = 7
#
#print (((3 + 2 + 1) - 5) + (((4 % 2) - (1 / 4)) + 6))
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# It seems that not:
#   5 < -2 = False
print "Is it true that 3 + 2 < 5 - 7"

# maths sequence:
#   3 + 2 = 5
#   5 - 5 = -2
#   5 < - 2 = false
#print (3 + 2) < (5 - 7)
print 3 + 2 < 5 - 7

# Breaking down the previous operation, by evaluating only the left side of it:
#   3 + 2 = 5
print "What is 3 + 2?", 3 + 2

# Breaking down the previous operation, by evaluating only the right side of it:
#   5 - 7 = -2
print "What is 5 - 7?", 5 - 7

# Oh yah 5 is not less then -2 ...
print "Oh, that's why it's False."

# Why not... this is fun ;)
print "How about some more."

# This one will be TRUE, once 5 is greater than -2
print "Is it greater?", 5 > -2

# And this will be also TRUE, once the condition greater or equal to (>=) can be satisfied
print "Is it greater or equal?", 5 >= -2

# No this is False once the condition less or equal to (<=), can't be satisfied.
print "Is it less or equal?", 5 <= -2
