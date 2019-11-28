# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)

'''
<script.py> output:
    nay_pep8.py:1:1: E265 block comment should start with '# '
    nay_pep8.py:2:6: E225 missing whitespace around operator
    nay_pep8.py:4:2: E131 continuation line unaligned for hanging indent
    nay_pep8.py:5:6: E131 continuation line unaligned for hanging indent
    nay_pep8.py:6:1: E122 continuation line missing indentation or outdented
    nay_pep8.py:7:1: E265 block comment should start with '# '
    nay_pep8.py:8:1: E402 module level import not at top of file
    nay_pep8.py:9:1: E265 block comment should start with '# '
    nay_pep8.py:10:1: E302 expected 2 blank lines, found 0
    nay_pep8.py:10:18: E231 missing whitespace after ','
    nay_pep8.py:11:2: E111 indentation is not a multiple of four
    nay_pep8.py:12:2: E111 indentation is not a multiple of four
    nay_pep8.py:14:1: E265 block comment should start with '# '
    nay_pep8.py:15:1: E305 expected 2 blank lines after class or function definition, found 1
    nay_pep8.py:16:11: E111 indentation is not a multiple of four
    nay_pep8.py:16:11: E117 over-indented
    nay_pep8.py:16:17: E225 missing whitespace around operator
    nay_pep8.py:16:32: E222 multiple spaces after operator
    nay_pep8.py:16:32: E251 unexpected spaces around keyword / parameter equals
    nay_pep8.py:16:38: E231 missing whitespace after ','
    nay_pep8.py:16:44: E221 multiple spaces before operator
    nay_pep8.py:16:44: E251 unexpected spaces around keyword / parameter equals
    nay_pep8.py:16:47: E251 unexpected spaces around keyword / parameter equals
    nay_pep8.py:17:11: E111 indentation is not a multiple of four
    nay_pep8.py:17:17: E201 whitespace after '('
    nay_pep8.py:17:25: E202 whitespace before ')'
    nay_pep8.py:17:27: W292 no newline at end of file
    {'E305': 'expected 2 blank lines after class or function definition, found 1', 'E265': 
    "block comment should start with '# '", 'E402': 'module level import not at top of file', 
    'E225': 'missing whitespace around operator', 'E222': 'multiple spaces after operator', 
    'E201': "whitespace after '('", 'E117': 'over-indented', 
    'E122': 'continuation line missing indentation or outdented', 
    'E302': 'expected 2 blank lines, found 0', 'E221': 'multiple spaces before operator', 
    'E111': 'indentation is not a multiple of four', 'E202': "whitespace before ')'", 
    'W292': 'no newline at end of file', 'E251': 'unexpected spaces around keyword / parameter equals', 
    'E131': 'continuation line unaligned for hanging indent', 'E231': "missing whitespace after ','"
    }
'''

In [1]: cat nay_pep8.py
'''
#define song lyric lines to tokenize
lines=[
  'Row, row, row your boat',
 'Gently down the stream',
     'Merrily, merrily, merrily, merrily',
'Life is but a dream']
#import needed packages
import re
#define helper function
def tokenize(text,regex):
 'function to tokenize text with a regex'
 return re.findall(regex, text)

#iterate over each line, tokenize, and print result
for line in lines:
          tokens=tokenize(text=  line,regex  = r'[a-zA-Z]+')
          print(  tokens )
'''


In [2]: cat yay_pep8.py
'''
# Import needed packages
import re


# Define helper function
def tokenize(text, regex):
    """function to tokenize text with a regex"""
    return re.findall(regex, text)
'''