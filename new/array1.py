# Implement a function to reverse an array.
# Write a program to find the sum of elements in an array.
# Implement an algorithm to find the maximum element in an array.

data = [1, 2, 3, 4, 5]
def reverse_arr(num):
    reverse_it=list(reversed(num))
    print(reverse_it)

def find_sum(num):
    a=sum(num)
    print(a)
def find_max(num):
    b=max(num)
    print(b)

# reverse_arr(data)
find_sum(data)
find_max(data)