# read an integer n
# Without using any string methods, try to print the following:
# 123...n

# Note that "..." represents the values in between

n = int(input())
for i in range(1, n+1):
    print(i, end="")