# How can I sort lines of text?

# As its name suggests, sort puts data in order. 
# By default it does this in ascending alphabetical order, 
# but the flags -n and -r can be used to sort numerically 
# and reverse the order of its output, while -b tells it to 
# ignore leading blanks and -f tells it to fold case 
# (i.e., be case-insensitive). Pipelines often use grep 
# to get rid of unwanted records and then sort to put the remaining records in order.


$ cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r
# wisdom
# wisdom
# wisdom
# wisdom
# molar
# molar
# molar


# Sorted! sort has many uses. For example, piping sort -n to head shows you the largest values.