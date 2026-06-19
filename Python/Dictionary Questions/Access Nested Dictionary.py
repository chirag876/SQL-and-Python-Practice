'''You are given a nested dictionary containing student details. Write a program to extract and print the marks of a given student.

Input:
student_data = {'John': {'age': 20, 'marks': 85}, 'Emma': {'age': 22, 'marks': 90}}
Student Name: "Emma"


Output:
90
'''


def access_nested_dict(studict, stuname):
    # Loop through each student and their details
    for name, details in studict.items():
        if name == stuname:
            # Return marks when the student is found
            return details['marks']


student_data = {
    'John': {'age': 20, 'marks': 85},
    'Emma': {'age': 22, 'marks': 90}
}

Name = "Emma"

marks = access_nested_dict(student_data, Name)
print(marks)  # Output: 90
