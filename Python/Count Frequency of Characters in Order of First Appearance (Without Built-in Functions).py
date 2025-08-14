'''Given a string s, count the frequency of each distinct character in the order in which they first appear in the string, without using any built-in frequency functions like count() or collections.Counter.

Input:  s = "abbbabcccce"  
Output: [2, 4, 4, 1]
'''


def countfrequency(strs):

    countlst = []
    visited = []  # keep track of already counted characters.

    for ch in strs:
        if ch not in visited:
            count = 0

            for char in strs:
                if ch == char:
                    count += 1

            countlst.append(count)
            visited += ch  # Add the character to visited.
    return countlst


s = "abbbabcccce"
print("Count of frequency of each character in the list:", countfrequency(s))
