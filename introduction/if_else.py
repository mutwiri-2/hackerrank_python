# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Constraints 1 <= n <= 100

n = 5  # alter this input  but Constraints 1 <= n <= 100

# my solution 
if n%2 == 1:
    print("Weird")
else:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")


# another solution better shorter solution
if n%2 == 0 and (n > 20 or n in range(2, 6)):
    print('Not Weird') 
else:
    print('Weird')