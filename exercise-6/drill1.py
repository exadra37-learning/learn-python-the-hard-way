# Exercise 6
#
# Drill 1:
#   Go through this program and write a comment above each line explaining it.

# NOTE:
#
# The Author suggestions in page 52 contradicts is own Initial suggestion on page 44 of the book:
#
# PDF Page 44 quote:
# Programmers use these variable names to make their code read more like English, and because they have lousy memories.
# If they didn't use good names for things in their software, they'd get lost when they tried to read their code again.
#
# PDF Page 52 Quote:
# You will also practice using short abbreviated variable names. Programmers love saving time at your expense by
# using annoyingly short and cryptic variable names, so let's get you started reading and writing them
# early on.
#
# So my preference goes for the first advice in page 44, and this can be called --> Semantic Programming <--.
#
# Please compare ex6.py with ex6-semantic-programming.py to understand the difference between writing a Semantic Program
#  and one that needs comments to explain what variable names should tell.
#
# Not a critic to the Author, just want to show that we can make our life, as Developers, more easy if we adopt Semantic
#  Programming.

# Assigning a string to the variable with a digit formatter, %d, that will contain the number for types of people.
#
# After the % in the end of the string we do not need to specify the values for the formatter inside parenthesis,
#  because we only have 1 formatter.
x = "There are %d types of people." % 10

# Assigning a string without any formatter to the variables.
binary = "binary"
do_not = "don't"

# At same time we assign a string to the variable we will use 2 string formatters, %s, to complete the string.
# Once we have more than 1 formatter, after the % in the end of string, we need to specify the variables to be used
#  by the formatters inside parenthesis, like (binary, do_not).
y = "Those who know %s and those who %s." % (binary, do_not)

# print the variables, x and y, contents to the screen without the need to assign the formatters, once that was already
#  done during the variable assignment of x and y.
print x
print y

# This an example of using the debug formatter %r to print to the screen the raw content of a variable.
# This formatter should be used only during development to check a variable.
print "I said: %r." % x

# Using a string formatter, %s, to complete the string at same time we print it to screen.
# We can see also the use of single quotes inside of double quotes when we wrap the formatter in single quotes '%s'.
# Once we only have 1 formatter we do not need to wrap the variable for it in parenthesis.
print "I also said: '%s'." % y

# Assigning a boolean value to a variable.
hilarious = False

# Assigning to the variable a string with a raw formatter, %r, used only for debug purposes.
# To notice here, that we use the formatter, but we do not assign the value to it yet.
# Each time this variable will be used, the value for %r formatter must be provided.
joke_evaluation = "Isn't that joke so funny?! %r"

# Once variable joke_evaluation contains a formatter place holder, the %r, we need to provide the value for it, what we
#  do with variable hilarious.
# Remember that this is a debug print, due to the use of %r formatter, therefore should be used only during development
#  and never shipped to production.
print joke_evaluation % hilarious

# Assigning a string to the variable without using any formatter.
w = "This is the left side of..."

# Assigning a string to the variable without using any formatter.
e = "a string with a right side."

# printing 2 variables to the screen by concatenating them with the plus(+) operator
# to note that his variables do not contain any formatter
print w + e
