"""
Problem: Calculate Average Marks

The provided code reads a dictionary containing key/value pairs of student name:[marks].
You are to print the average of the marks array for the student name provided, showing
2 places after the decimal.

Input Format:
- The first line contains the integer n, the number of students' records.
- The next n lines contain the name and the marks obtained by that student, 
  separated by a space. The marks are floating point numbers and there are exactly 3 marks per student.
- The final line contains the query_name, the name of the student whose average marks need to be printed.

Output Format:
- Print one line: The average of the marks obtained by the particular student 
  correct to 2 decimal places.

Sample Input 0:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0:
56.00
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")


# python provides in built method for swapcase conversion
# str.swapcase() converts all uppercase letters to lowercase and vice versa.
# Example:
# s = "Hello World"
# print(s.swapcase())  # Output: "hELLO wORLD"
