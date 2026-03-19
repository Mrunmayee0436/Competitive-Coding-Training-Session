# Replacing a string with another string

# Example 1
s = "This is a difficult problem."
s1 = s.replace("difficult", "easy")
print(s1)  # Output: This is a easy problem.

# Example 2: All occurrences will be replaced
s = "ababababababab"
s1 = s.replace("a", "b")
print(s1)  # Output: bbbbbbbbbbbbbb
