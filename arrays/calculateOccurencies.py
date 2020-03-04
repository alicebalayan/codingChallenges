'''
Problem: 
Write a Python program to get the number of occurrences of a specified element in an array. 

From (#6): https://www.w3resource.com/python-exercises/array/ 
'''

a1 = [11, 23, 50, 23, 100, 100, 100]
specified1 = 100

def occurence(input_array, target):
    count = 0
    for i in range(len(input_array)):
        if target == input_array[i]:
            count += 1
    return count

print(occurence(a1, specified1))