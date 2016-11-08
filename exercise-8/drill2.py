# Exercise 8
#
# Drill 2:
#   Notice that the last line of output uses both single-quotes and double-quotes for individual pieces.
#   Why do you think that is?

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Reply to the question of this Drill
print "\nAs we can see in the previous line, every time the formatter %r prints a string containing a single quote",
print "it will wrap the whole string in double quotes."
