'''
*Write function that takes two args: list of strings and a prefix (string). 
The function should iterate over the list and find all strings which start with the prefix, 
then return list of such strings
'''

def str_prefix(str_list, prefix):
    good_list = []
    for str in str_list:
        if str[0 : len(prefix)] == prefix :
            good_list.append(str)
    return good_list

print(str_prefix(["absolutely", "Manchester", "abdominal", "absent", "ant"], "ab"))
# ['absolutely', 'abdominal', 'absent']