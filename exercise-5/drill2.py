# Exercise 5
#
# Drill 2:
#   Try to write some variables that convert the inches and pounds to centimetres and kilograms. Do not just type in the
#    measurements. Work out the math in Python.

inches_to_centimetres_conversion = 2.54
libras_to_kilograms_conversion = 0.453592

author_name = 'Zed A. Shaw'
author_age = 35 # not a lie
author_height_in_inches = 74 # a better variable name dispenses the previous comment on this line in ex5.py
author_height_in_centimetres = author_height_in_inches * inches_to_centimetres_conversion
author_weight_in_libras = 180 # same here about comments to explain variables
author_weight_in_kilograms = author_weight_in_libras * libras_to_kilograms_conversion
author_eyes_colour = 'Blue'
author_teeth_colour = 'White'
author_hair_colour = 'Brown'

print "Let's talk about %s." % author_name
print "He's %d inches tall." % author_height_in_inches
print "He's %d centimetres tall." % author_height_in_centimetres
print "He's %d pounds heavy." % author_weight_in_libras
print "He's %d kilograms heavy." % author_weight_in_kilograms
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (author_eyes_colour, author_hair_colour)
print "His teeth are usually %s depending on the coffee." % author_teeth_colour

# this line is tricky, try to get exactly right
print "If I add %d, %d, and %d I get %d." % (author_age, author_height_in_inches, author_weight_in_libras, author_age + author_height_in_inches + author_weight_in_libras)
