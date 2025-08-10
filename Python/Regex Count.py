import re

# inputstring = input("Enter a string: ")
inputstring = 'f; u{}34  '
digitcount = re.sub("[^0-9]", "", inputstring)

lettercount = re.sub("[^a-zA-Z]", "", inputstring)

spacecount = re.findall("[ \n]", inputstring)

print("The number of digits in the string is:", len(digitcount))
print("The number of letters in the string is:", len(lettercount))
print("The number of spaces in the string is:", len(spacecount))
