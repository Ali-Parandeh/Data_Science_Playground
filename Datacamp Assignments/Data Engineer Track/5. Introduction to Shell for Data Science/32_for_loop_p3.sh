$ datasets=seasonal/*csv

$ echo $datasets
# seasonal/autumn.csv seasonal/spring.csv seasonal/summer.csv seasonal/winter.csv

$ for filename in $datasets; do echo $filename; done
# seasonal/autumn.csv
# seasonal/spring.csv
# seasonal/summer.csv
# seasonal/winter.csv