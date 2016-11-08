# Exercise 8
#
# Drill 1:
#   Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.

# So checks performed and no mistakes found, but I will comment each line of code as usual.
#
# Comment each line of code helps us memorize what we are learning... I am founding this technique very effective
#   to retain all the info absorbed until now.

# assigning to a variable several debug formatters %r, so that we can reuse the formatters
formatter = "%r %r %r %r"

# print to screen a string made only from filling the %r formatters with integers
print formatter % (1, 2, 3, 4)

# print to screen a string made only from filling the %r formatters with other strings
print formatter % ("one", "two", "three", "four")

# print to screen a string made only from filling the %r formatters with Boolean values
print formatter % (True, False, False, True)

# print to screen a string made only from filling the %r formatters with the formatter variable itself.
# so this means that formatters inside of a string are treated as normal characters, unless the % character are found
#   in the end of the print sentence, when it must be followed by the same number of variables as formatters inside
#   the string.
print formatter % (formatter, formatter, formatter, formatter)

# Multi-line assignment of values to the formatters
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
