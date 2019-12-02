# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12, 2)]
print(nums_list2)


'''
<script.py> output:
    <class 'range'>
    [0, 1, 2, 3, 4, 5]
    [1, 3, 5, 7, 9, 11]
    
Notice that using Python's range() function allows you to create a range object of 
numbers without explicitly typing them out. You can convert the range object into a 
list by using the list() function or by unpacking it into a list using the star character (*).
'''