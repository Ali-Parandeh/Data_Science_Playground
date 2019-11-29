'''
Below is the structure of where you'll be working.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
│    ├── document.py
└── my_script.py
'''

# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text


'''
You just completed writing the Document class for your package in document.py. 
Which of the following lines would correctly import this class in __init__.py 
using relative import syntax?
'''

from .document import Document