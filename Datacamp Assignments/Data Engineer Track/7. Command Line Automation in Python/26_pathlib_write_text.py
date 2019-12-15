# File writing one-liner

# As a Data Engineer at a Fortune 500 company you need to make sure your 
# large scale data pipeline is running smoothly. Recently you have been 
# experienced unpredictable errors when running Spark Python jobs. 
# You want to write an integration test that programatically creates 
# Python files, gives them executable permission and the runs them. 
# You want to run this everytime you create IaC (Infrastructure as Code) 
# scripts that provision new Spark clusters.

# Create an integration script that creates several Python files and 
# writes Python to them. After that run them all with python3 and 
# subprocess to obtain the scripts' output. The Path module is imported for you.

# 1. Use pathlib.write_text to write to create and write files.
# 2. Use Path and .glob to find these files.
# 3. Run all the matching python scripts using subprocess.run method.

from subprocess import run, PIPE
from pathlib import Path

# Find all the python files you created and print them out
for i in range(3):
  path = Path(f"/tmp/test/file_{i}.py")
  path.write_text("#!/usr/bin/env python\n")
  path.write_text("import datetime;print(datetime.datetime.now())")
  

# Find all the python files you created and print them out
for file in Path("/tmp/test/").glob("*.py"):
  # gets the resolved full path
  fullpath = str(file.resolve())
  proc = run(["python3", fullpath], stdout=PIPE)
  print(proc)


# <script.py> output:
#     CompletedProcess(args=['python3', '/tmp/test/file_1.py'], returncode=0, stdout=b'2019-12-15 00:05:55.030747\n')
#     CompletedProcess(args=['python3', '/tmp/test/file_0.py'], returncode=0, stdout=b'2019-12-15 00:05:55.061972\n')
#     CompletedProcess(args=['python3', '/tmp/test/file_2.py'], returncode=0, stdout=b'2019-12-15 00:05:55.088454\n')


# Great work writing Python that writes Python. 
# Think about that for a second! You used the pathlib module to 
# do much of the heavy lifting to create Python scripts and then you used subprocess to verify them all.

