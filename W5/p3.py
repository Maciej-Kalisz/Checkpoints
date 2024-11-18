# A string P is a prefix of another string S when S starts with P. For example, “turn” is a prefix of “turnover”.
# Write in the box below a method is_prefix that takes two strings arguments. It should return True or False depending on whether the first string is a prefix of the second.
# Your answer should be implemented using a for loop that checks whether each character of the first string is equal to the character at the same position in the second string.
# Recall that you can obtain the length of a string with the len function. You can get the character position i in a string s with s[i].
# Remember that the first character in a string is at position (or index) zero!
# Be careful to first check that the length of the first string is less than or equal to that of the second string, otherwise you may encounter an error.
# Note: that you can return a value for a function from inside a for loop.
def is_prefix(sub_string: str, full_string: str) -> bool:
    if len(sub_string) > len(full_string):
        return False

    elif sub_string == full_string:
        return True

    else:
        for i in range(len(sub_string)):
            if sub_string[i] != full_string[i]:
                return False

        return True
