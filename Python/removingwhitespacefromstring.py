def removingwhiltespace(str):
    return str.replace(" ", "")

str1 = "My name is chirag"
print(removingwhiltespace(str1))

def removingwhiltespace(str):
    inputstr = str.split()
    outputstr = "".join(inputstr)
    return outputstr

str2 = "My name is aman"
print(removingwhiltespace(str2))

