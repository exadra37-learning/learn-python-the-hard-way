author_name = 'Zed A. Shaw'
author_age = 35 # not a lie
author_height_in_inches = 74 # a better variable name dispenses the previous comment on this line in ex5.py
author_weight_in_lbs = 180 # same here about comments to explain variables
author_eyes_colour = 'Blue'
author_teeth_colour = 'White'
author_hair_colour = 'Brown'

print "Let's talk about %s." % author_name
print "He's %d inches tall." % author_height_in_inches
print "He's %d pounds heavy." % author_weight_in_lbs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (author_eyes_colour, author_hair_colour)
print "His teeth are usually %s depending on the coffee." % author_teeth_colour

# this line is tricky, try to get exactly right
print "If I add %d, %d, and %d I get %d." % (author_age, author_height_in_inches, author_weight_in_lbs, author_age + author_height_in_inches + author_weight_in_lbs)
