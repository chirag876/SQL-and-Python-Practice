'''Given a dictionary containing names as keys and scores as values, write a program to print the names of the top 3 scorers in descending order of their scores

Input:
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 79, 'Eve': 95}

Output:

[('Eve', 95), ('Bob', 92), ('Charlie', 88)]

'''
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 79, 'Eve': 95}

topthree = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
print(topthree)
