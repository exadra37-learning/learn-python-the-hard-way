# SEMANTIC PROGRAMMING

# NOTE: In drill1.py you can see also a note about the Author contradictions regarding variable names.
#       In this script I follow the first Author advice to choose variables names that make the read of code more like
#        English.
#       This approach can be called of Semantic Programming and when we adhere to it the code will be more easy to read,
#        understand and use.
#       Please compare this script with drill1.py where comments are need to explain what variable names should tell.
#       Also you can compare this script with ex6.py to see how it is much more readable when you adhere to
#        Semantic Programming.
#       This is not a critic to the Author, just a way of making easier for you or any Developer to later on come back
#        to the code and grasp it quickly.

types_of_people = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
people_knowledge = "Those who know %s and those who %s." % (binary, do_not)

print types_of_people
print people_knowledge

print "I said: %r." % types_of_people
print "I also said: '%s'." % people_knowledge

is_hilarious = False

# using %r formatter to debug variable is_hilarious
# should only be use during development, not in production
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % is_hilarious

left_of_string = "This is the left side of..."
right_of_string = "a string with a right side."

print left_of_string + right_of_string
