# Exercise 9
#
# Drill 1:
#   Check your work, write down your mistakes, try not to make them on the next exercise.

# Checks done and no errors found.
#
# Commenting what each line of code does as usual.

# Here's some new strange stuff, remember type it exactly.

# assigning a plain string, without any formatter or special character to the variable.
days = "Mon Tue Wed Fri Sat Sun"

# using the special character for new line(\n) in the string we are assigning
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# using print to output a variable with a plain string
print "Here are the days: ", days

# output a variable that contains new lines(\n) between each word
print "Here are the months: ", months

# using triple quotes to allow us to span our text freely across multiple lines without the need to use the command
#  print in each line.
# when we output to the screen we will see it exactly as how we wrote it.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# The use of triple quotes to write free text is called in other language Herege Docs
print """
---> Try to use formatter %r to print variable months <---

>>> print "%r" % months""" # closing triple quotes here will not create a new line

# lets debug variable months to see is raw output
print "%r" % months

# explaining the result of debugging variable months
print """
As we can see the new lines in variable months have no effect.

This is because formatter %r is to display the raw content of a variable, therefore special characters loose there
 special meaning.
"""
