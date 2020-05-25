# You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and marks for n students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

# Input Format
# The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

# Constraints
# 2<=n<=10
# 0<=marks<=100

# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0
# 56.00

# Sample Input 1
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

# Sample Output 1
# 26.50

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

student_marks = {
    'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60],
}

query_name = 'Malika'

marks = student_marks.get(query_name)
average = sum(marks) / len(marks)
print(format(average, ".2f"))
