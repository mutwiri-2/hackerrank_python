# Read two integers from STDIN and print three lines where:

# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.

a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

# Read two integers and print two lines. The first line should contain integer division. The second line should contain float division

c = int(input())
d = int(input())

print(c//d)  #integer division
print(c/d)  #float division