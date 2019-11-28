# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Ali',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])


'''
<script.py> output:
    running bdist_rpm
    running egg_info
    creating text_analyzer.egg-info
    writing text_analyzer.egg-info/PKG-INFO
    writing dependency_links to text_analyzer.egg-info/dependency_links.txt
    writing top-level names to text_analyzer.egg-info/top_level.txt
    writing manifest file 'text_analyzer.egg-info/SOURCES.txt'
    reading manifest file 'text_analyzer.egg-info/SOURCES.txt'
    writing manifest file 'text_analyzer.egg-info/SOURCES.txt'
    creating dist
    writing 'dist/text_analyzer.spec'

When users pip install your package the correct version of matplotlib will be automatically handled by pip.
You can now pip install your package and even publish it to PyPi!
'''