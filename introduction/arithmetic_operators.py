# Read two integers from STDIN and print three lines where:

# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.

a = int(input("enter any integer: "))
b = int(input("enter another integer: "))

print("The sum of the integers is: ",a+b)
print("The difference between the integers is:",a-b)
print("The product of the integers is:" ,a*b)

# Read two integers and print two lines. The first line should contain integer
# division. The second line should contain float division

c = int(input("Enter an integer1: "))
d = int(input("Enter another integer2: "))

print("integer1 // integer2 equals", c//d)  #integer division
print("integer1 / integer2 equals ", c/d)  #float division