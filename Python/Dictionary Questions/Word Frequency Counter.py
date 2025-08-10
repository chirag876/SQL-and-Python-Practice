'''Given a string S consisting of words separated by spaces, write a program to count the frequency of each word and store the result in a dictionary. The words should be case-sensitive.

Input: S = "apple banana apple orange banana apple"

Output = {'apple': 3, 'banana': 2, 'orange': 1}

'''


def wordfrequencycountforstringinput(strs):
    freqcount = {}
    wordsplit = strs.split(" ")

    for char in wordsplit:
        if char in freqcount:
            freqcount[char] += 1
        else:
            freqcount[char] = 1
    return freqcount


S = "apple banana apple orange banana apple"
print("Frequency count for string input:", wordfrequencycountforstringinput(S))


def wordfrequencycountforlistinput(lst):
    lstfreqcount = {}

    for char in lst:
        if char in lstfreqcount:
            lstfreqcount[char] += 1
        else:
            lstfreqcount[char] = 1
    return lstfreqcount


lst = ["apple", "banana", "orange", "banana"]
print("Frequency count for lst input:", wordfrequencycountforlistinput(lst))
