$ for f in seasonal/*csv; do echo $f; head -n 2 $f | tail -n 1; done

# seasonal/autumn.csv
# 2017-01-05,canine
# seasonal/spring.csv
# 2017-01-25,wisdom
# seasonal/summer.csv
# 2017-01-11,canine
# seasonal/winter.csv
# 2017-01-03,bicuspid

$ for f in seasonal/*csv; do echo $f head -n 2 $f | tail -n 1; done

# seasonal/autumn.csv head -n 2 seasonal/autumn.csv
# seasonal/spring.csv head -n 2 seasonal/spring.csv
# seasonal/summer.csv head -n 2 seasonal/summer.csv
# seasonal/winter.csv head -n 2 seasonal/winter.csv

$ for f in seasonal/*csv; do echo $f | head -n 2 $f | tail -n 1; done

# 2017-01-05,canine
# 2017-01-25,wisdom
# 2017-01-11,canine
# 2017-01-03,bicuspid