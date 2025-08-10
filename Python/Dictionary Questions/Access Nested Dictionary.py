'''You are given a nested dictionary containing student details. Write a program to extract and print the marks of a given student.

Input:
student_data = {'John': {'age': 20, 'marks': 85}, 'Emma': {'age': 22, 'marks': 90}}
Student Name: "Emma"


Output:
90
'''


def accessnesteddictionary(studict, stuname):
    for name, details in studict.items():
        if name == stuname:
            return details['marks']


student_data = {'John': {'age': 20, 'marks': 85},
                'Emma': {'age': 22, 'marks': 90}}
Name = "Emma"

marks = accessnesteddictionary(student_data, Name)
print(marks)
print
