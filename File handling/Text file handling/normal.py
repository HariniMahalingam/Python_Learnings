#normal reading an file
file = open("normal.txt", "r")
content = file.read() #read() - returns the entire content as a string.
print(content)
file.close()