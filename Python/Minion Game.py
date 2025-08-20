"""
HackerRank Problem: The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
- Both players are given the same string, S.
- Both players have to make substrings using the letters of the string S.
- Stuart has to make words starting with consonants.
- Kevin has to make words starting with vowels (A, E, I, O, U).
- The game ends when both players have made all possible substrings.

Scoring:
- A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 points.

Your task is to determine the winner of the game and their score.

Function Description:
Complete the minion_game function in the editor below.

minion_game has the following parameters:
    - string string: the string to analyze

Prints:
    - string: the winner's name and score, separated by a space, 
              or "Draw" if there is no winner

Input Format:
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A-Z].

Constraints:
0 < len(S) <= 10^6

Output Format:
Print one line:
    - "Kevin <score>" if Kevin wins
    - "Stuart <score>" if Stuart wins
    - "Draw" if there is no winner

Sample Input:
BANANA

Sample Output:
Stuart 12
"""


def minion_game(string):
    vowels = "AEIOU"
    ksc = 0
    ssc = 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            ksc += len(string)-i
        else:
            ssc += len(string)-i
    if ksc > ssc:
        print("Kevin", ksc)
    elif ssc > ksc:
        print("Stuart", ssc)
    else:
        print("Draw")


s = "BANANA"
minion_game(s)
