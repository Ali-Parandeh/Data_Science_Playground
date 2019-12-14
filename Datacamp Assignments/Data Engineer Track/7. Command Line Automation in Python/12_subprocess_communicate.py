# Waiting for processes

# In the real-world code is messy. There are edge cases that have to be handled, 
# and things don't always go as planned. Dealing with data increases the complexity of the mess.

# In this example you will be using the subprocess module to launch a 
# "misbehaving" process that will run for six seconds. This will be 
# simulated by using linux sleep command. The sleep command will 
# suspend execution of a shell for a period of time. You will use 
# the subprocess.communicate() method to wait for the command to 
# finish running for up to five seconds. The process will then 
# timeout and it will return an Exception: i.e. error detected 
# during execution, which will be caught and the process will 
# be cleaned up by proc.kill(). Popen, PIPE, and TimeoutExpired have all been imported for you.

# 1. Start a long running process using subprocess.Popen().
# 2. Use subprocess.communicate() to create a timeout.
# 3. Cleanup the process if it takes longer than the timeout.
# 4. Print error message and standard out and standard error streams.


from subprocess import (PIPE, Popen)

# Start a long running process using subprocess.Popen()
proc = Popen(["sleep", "6"], stdout=PIPE, stderr=PIPE)

# Use subprocess.communicate() to create a timeout 
try:
    output, error = proc.communicate(timeout=5)
    
except TimeoutExpired:

	# Cleanup the process if it takes longer than the timeout
    proc.kill()
    
    # Read standard out and standard error streams and print
    output, error = proc.communicate()
    print(f"Process timed out with output: {output}, error: {error}")

# <script.py> output:
#     Process timed out with output: b'', error: b''


# You were able to catch the process as it timed out. 
# The 'rogue' process was killed by using proc.kill() when 
# the TimeoutExpired exception was triggered. You may want to 
# experiment with altering the timeout to be shorter or longer to see what happens.