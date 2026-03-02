# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.


def abbrev_name(name):
    initials = name.split()
    return initials[0][0].upper() + "." + initials[1][0].upper()
