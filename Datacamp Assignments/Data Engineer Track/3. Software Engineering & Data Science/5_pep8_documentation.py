def print_phrase(phrase, polite=True, shout=False):
    if polite:# It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  #All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


#Politely ask for help
print_phrase('help me', polite=True)
 # Shout about a discovery
print_phrase('eureka', shout=True)


'''
my_script.py:2:15: E261 at least two spaces before inline comment
my_script.py:5:16: E262 inline comment should start with '# '
my_script.py:11:1: E265 block comment should start with '# '
my_script.py:13:2: E114 indentation is not a multiple of four (comment)
my_script.py:13:2: E116 unexpected indentation (comment)
'''


def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)



'''
Nicely formatted comments can provide a lot value to help collaborators easily read the documentation you've left for th
'''