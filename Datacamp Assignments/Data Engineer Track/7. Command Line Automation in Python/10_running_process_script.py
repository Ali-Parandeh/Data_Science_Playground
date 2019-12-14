# Running processes script

# One day your boss asks you to monitor CPU usage. 
# They suspect someone is using CPU processing power to 
# run other code instead of writing unit tests.

# Write a script using subprocess.run and ps aux that discards 
# all CPU output with the string 'python' in it. 

import subprocess

# Use subprocess to run the `ps aux` command that lists running processes
with subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE) as proc:
    process_output = proc.stdout.readlines()
    
# Look through each line in the output and skip it if it contains "python"
for line in process_output:
    # b'python' because a bytes-like object is required, not 'str'
    if b'python' in line:
        continue
    print(line)


# <script.py> output:
#     b'USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\n'
#     b'repl        35  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>\n'
#     b'repl        43  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>\n'
#     b'repl        45  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>\n'
#     b'repl        51  0.0  0.0      0     0 pts/0    Z+   16:21   0:00 [ls] <defunct>\n'
#     b'repl        57  0.0  0.0      0     0 pts/0    Z+   16:21   0:00 [ls] <defunct>\n'
#     b'repl        63  0.0  0.0      0     0 pts/0    Z+   16:22   0:00 [ls] <defunct>\n'
#     b'repl        69  0.0  0.0      0     0 pts/0    Z+   16:22   0:00 [ls] <defunct>\n'
#     b'repl        75  0.0  0.0      0     0 pts/0    Z+   16:22   0:00 [ls] <defunct>\n'
#     b'repl        81  0.0  0.0      0     0 pts/0    Z+   16:24   0:00 [ls] <defunct>\n'
#     b'repl       101  0.0  0.0      0     0 pts/0    Z+   16:32   0:00 [touch] <defunct>\n'
#     b'repl       103  0.0  0.0      0     0 pts/0    Z+   16:52   0:00 [touch] <defunct>\n'
#     b'repl       109  0.0  0.0      0     0 pts/0    Z+   16:52   0:00 [touch] <defunct>\n'
#     b'repl       111  0.0  0.0      0     0 pts/0    Z+   16:52   0:00 [touch] <defunct>\n'
#     b'repl       117  0.0  0.0      0     0 pts/0    Z+   16:53   0:00 [touch] <defunct>\n'
#     b'repl       118  0.0  0.0      0     0 pts/0    Z+   16:55   0:00 [touch] <defunct>\n'
#     b'repl       119  0.0  0.0      0     0 pts/0    Z+   16:55   0:00 [touch] <defunct>\n'
#     b'repl       120  0.0  0.0      0     0 pts/0    Z+   16:55   0:00 [touch] <defunct>\n'
#     b'repl       217  0.0  0.0      0     0 pts/0    Z+   17:05   0:00 [ps] <defunct>\n'
#     b'repl       218  0.0  0.0      0     0 pts/0    Z+   17:05   0:00 [ps] <defunct>\n'
#     b'repl       260  0.0  0.0  36072  3284 pts/0    R+   17:12   0:00 ps aux\n'


In [32]: !ps
#   PID TTY          TIME CMD
#   256 pts/1    00:00:00 sh
#   257 pts/1    00:00:00 ps

In [33]: !ps aux
# USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# repl         1  0.0  0.3 979636 59516 pts/0    Ssl+ 16:08   0:03 python3 -i
# repl        35  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>
# repl        43  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>
# repl        45  0.0  0.0      0     0 pts/0    Z+   16:20   0:00 [ls] <defunct>


