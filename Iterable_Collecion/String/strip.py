# Strip function is used to remove the leading and trailing whitespaces.
"""
Strips are used remove to remove in both full, right and left side
1. special characters
2. string characters
Syntax
string.strip(substring(optional))
Additional info
1) string.strip()
will all remove the whitespace,\n at the start and at the end.
2) string.strip(sub_string)
strip with charater
it will traverse from left and when first mismatch occurs , it will stop strip operation to the rest of the string positions
it will traverse from right and when first mismatch occurs , it will stop strip operation to the rest of the string positions
since only .strip() is given both left & right will be considered.

"""
text = "    The unwanted space   "
print(text)
stripped_text = text.strip()
left_stripped = text.lstrip()
right_stripped = text.rstrip()
print("Stripped Text:",stripped_text)
print("Left Stripped Text :",left_stripped)
print("Right Stripped Text :",right_stripped)
