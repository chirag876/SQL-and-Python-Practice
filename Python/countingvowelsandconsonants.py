# def countingvowels(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0

#     for char in word:
#         if char in vowels:
#             count +=1
#     return count

# string1 = "Chirag"
# print("Count of Vowels:", countingvowels(string1))

def countingconsonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelcount = 0
    consonantscount = 0
    for char in word:
        if char in vowels:
            vowelcount += 1
        else:
            consonantscount += 1
    return vowelcount, consonantscount


string1 = "Chirag"
vowels, consonants = countingconsonants(string1)
print("Count of consonants:", consonants)
print("Count of vowels:", vowels)
