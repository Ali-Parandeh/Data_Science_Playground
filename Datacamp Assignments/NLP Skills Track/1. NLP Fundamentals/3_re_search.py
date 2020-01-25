# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())
# 580 588

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))
# <_sre.SRE_Match object; span=(9, 32), match='[wind] [clop clop clop]'>

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[A-z]+:"
print(re.search(pattern2, sentences[3]))
# <_sre.SRE_Match object; span=(0, 7), match='ARTHUR:'>
