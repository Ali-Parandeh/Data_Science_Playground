#  To find out what commands do, people used to use the man command (short for "manual"). 
#  man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.
#  The problem with the Unix manual is that you have to know what you're looking for. 

$ man head

# HEAD(1)               BSD General Commands Manual              HEAD(1)

# NAME
#      head -- display first lines of a file

# SYNOPSIS
#      head [-n count | -c bytes] [file ...]

# DESCRIPTION
#      This filter displays the first count lines or bytes of each of
#      the specified files, or of the standard input if no files are
#      specified.  If count is omitted it defaults to 10.

#      If more than a single file is specified, each file is preceded by
#      a header consisting of the string ``==> XXX <=='' where ``XXX''
#      is the name of the file.

# SEE ALSO
#      tail(1)