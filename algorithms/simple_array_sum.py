# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1,2,3], 1+2+3 , so return 6. 

def simple_array_sum(ar):
    return sum(ar)

num = [1, 6, 7, 8, 8, 9, 5, 4]
squares = [i**2 for i in range(1,10)]
print(simple_array_sum(num))
print(simple_array_sum(squares))