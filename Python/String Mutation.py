'''We all know that strings are immutable (they cannot be changed) but what if we want to insert a value in the string at a specific index say index 5 so you task it to insert a value in the string at a specific index 

Input s = 'abracadabra', charactertoinsert, positiontowhichtoinsertthecharacter,

output: s ='abrackadbar'
'''


def mutationstring(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string


s = 'abracadabra'
position = 5
character = 'k'

print("Final string after inserting the character:",
      mutationstring(s, position, character))
