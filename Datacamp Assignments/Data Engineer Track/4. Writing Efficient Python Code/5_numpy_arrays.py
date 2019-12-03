nums = [[ 1,  2,  3,  4,  5], 
        [ 6,  7,  8,  9, 10]]

# Print second row of nums
print(nums[1,:])

'''
[ 6  7  8  9 10]
'''

# Print all elements of nums that are greater than six
print(nums[nums > 6])

'''
[ 7  8  9 10]
'''

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

'''
[[ 2  4  6  8 10]
 [12 14 16 18 20]]
'''

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

'''
[[ 1  2  4  4  5]
 [ 6  7  9  9 10]]
'''

'''
Using numpy arrays allows you to take advantage of an array's memory efficient nature and easily perform mathematical operations on your data.
'''