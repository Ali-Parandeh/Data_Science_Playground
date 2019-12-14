# Running a health check

# The data science team at your company has been working closely with 
# the DevOps team to ensure the production machine learning systems are 
# reliable, elastic and fault-tolerant. Recently, there was an outage of 
# a critical system that cost the company hundreds of thousands of dollars 
# in lost revenue when a machine learning model began throwing exceptions 
# instead of offering recommendations to shoppers. One solution that can be
#  implemented is to run periodic health checks on production systems to 
#  ensure they have the correct environment. The DevOps team has written 
#  several bash scripts that your team will need to invoke from Python and run periodically.

# Send the output of an echo 'python3' command to a healthcheck.sh script.


import subprocess

# equivalent to 'echo "python3"'
echo = subprocess.Popen(
    ["echo", "python3"], stdout=subprocess.PIPE)

# equivalent to: echo "python3" | ./healthcheck.sh
path = subprocess.Popen(
    ["./healthcheck.sh"], stdin=echo.stdout, stdout=subprocess.PIPE)

full_path = path.stdout.read().decode("utf-8")
print(f"...Health Check Output...\n\n {full_path}")

# The assertion will fail if python3 executable path is not found
assert "python3" in full_path

# <script.py> output:
#     ...Health Check Output...
    
#      Enter executable to check: 
#     Location: /usr/bin/python3

# Great job building a health check utility! You were able to 
# validate that python3 was installed and assert it. Monitoring 
# tasks like these are an essential DevOps best practice and 
# DevOps best practices heavily influence work in Data Engineering and Machine Learning.