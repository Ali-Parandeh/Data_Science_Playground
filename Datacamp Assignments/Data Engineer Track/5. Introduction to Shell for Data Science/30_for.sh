# How can I repeat a command many times?

# Shell variables are also used in loops, which repeat commands many times. If we run this command:

for filetype in gif jpg png; do echo $filetype; done

# it produces:

# gif
# jpg
# png

# Notice these things about the loop:

# The structure is for ...variable... in ...list... ; do ...body... ; done
# The list of things the loop is to process 
# (in our case, the words gif, jpg, and png).
# The variable that keeps track of which thing 
# the loop is currently processing (in our case, filetype).
# The body of the loop that does the processing 
# (in our case, echo $filetype).
# Notice that the body uses $filetype to get the 
# variable's value instead of just filetype, just 
# like it does with any other shell variable. Also 
# notice where the semi-colons go: the first one 
# comes between the list and the keyword do, and 
# the second comes between the body and the keyword done.

$ for filetype in docx odt pdf; do echo $filetype; done
# docx
# odt
# pdf