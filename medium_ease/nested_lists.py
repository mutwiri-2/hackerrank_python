# Given the names and grades for each object in a Physics class of n students, store them in a nested list and print the name(s) of any object(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, n, the number of students.
# The 2n subsequent lines describe each object over 2 lines; the first line contains a object's name, and the second line contains their grade.

# Constraints
# 2<=n<=5
# There will always be one or more students having the second lowest grade.

# Output Format

# Print the name(s) of any object(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
# Berry
# Harry

# Explanation 0
# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# if __name__ == '__main__':
#     physics_results = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

#         physics_results.append([name,score])
    
#     # print(physics_results)
#     results = []
#     names, marks = zip(*physics_results)
#     second_lowest = sorted(list(marks))[-2]
#     for object in physics_results:
#         for name, mark in object:
#             if mark == second_lowest:
#                 results.append(name)
#     print('\n'.join(sorted(results, key=str.lower)))

physics_results = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
second_lowest_list = []
names, marks = zip(*physics_results)
second_lowest = sorted(list(set(marks)))[1] # remove duplicates, sort and get the second element
for object in physics_results:
    if object[1] == second_lowest: 
        second_lowest_list.append(object[0])
sorted_names = sorted(second_lowest_list, key=str.lower)
print('\n'.join(sorted_names))
# print('\n'.join(sorted(results, key=str.lower)))
            
