In [1]: ls
# src/

In [2]: ls src/
# apple103.txt  apple94.txt    banana52.txt       blackberry87.txt  pear108.txt
# apple109.txt  apple99.txt    banana53.txt       blackberry8.txt   pear10.txt
# apple117.txt  apple.py       banana57.txt       blackberry95.txt  pear110.txt
# apple118.txt  banana102.txt  banana5.txt        blackberry98.txt  pear114.txt
# apple124.txt  banana104.txt  banana60.txt       orange113.txt     pear116.txt
# apple131.txt  banana106.txt  banana61.txt       orange115.txt     pear127.txt
# apple132.txt  banana111.txt  banana66.txt       orange120.txt     pear128.txt
# apple134.txt  banana112.txt  banana67.txt       orange121.txt     pear130.txt
# apple135.txt  banana119.txt  banana70.txt       orange139.txt     pear137.txt
# apple142.txt  banana11.txt   banana76.txt       orange13.txt      pear138.txt
# apple147.txt  banana122.txt  banana80.txt       orange153.txt     pear140.txt
# apple149.txt  banana123.txt  banana82.txt       orange162.txt     pear143.txt
# apple150.txt  banana12.txt   banana84.txt       orange163.txt     pear144.txt
# apple15.txt   banana133.txt  banana89.txt       orange173.txt     pear145.txt
# apple160.txt  banana14.txt   banana90.txt       orange186.txt     pear146.txt
# apple169.txt  banana151.txt  banana.py          orange188.txt     pear154.txt
# apple16.txt   banana152.txt  blackberry105.txt  orange195.txt     pear155.txt
# apple170.txt  banana158.txt  blackberry125.txt  orange196.txt     pear156.txt
# apple17.txt   banana159.txt  blackberry126.txt  orange200.txt     pear166.txt
# apple182.txt  banana167.txt  blackberry129.txt  orange201.txt     pear172.txt
# apple183.txt  banana168.txt  blackberry136.txt  orange213.txt     pear175.txt
# apple184.txt  banana176.txt  blackberry141.txt  orange215.txt     pear180.txt
# apple189.txt  banana177.txt  blackberry148.txt  orange217.txt     pear181.txt
# apple190.txt  banana179.txt  blackberry157.txt  orange223.txt     pear194.txt
# apple193.txt  banana185.txt  blackberry161.txt  orange224.txt     pear199.txt
# apple198.txt  banana18.txt   blackberry164.txt  orange228.txt     pear1.txt
# apple202.txt  banana191.txt  blackberry165.txt  orange22.txt      pear208.txt
# apple204.txt  banana192.txt  blackberry171.txt  orange233.txt     pear212.txt
# apple219.txt  banana197.txt  blackberry174.txt  orange236.txt     pear214.txt
# apple229.txt  banana205.txt  blackberry178.txt  orange237.txt     pear220.txt
# apple234.txt  banana206.txt  blackberry187.txt  orange248.txt     pear222.txt
# apple239.txt  banana207.txt  blackberry19.txt   orange24.txt      pear226.txt
# apple23.txt   banana209.txt  blackberry203.txt  orange27.txt      pear227.txt
# apple240.txt  banana20.txt   blackberry211.txt  orange28.txt      pear235.txt
# apple242.txt  banana210.txt  blackberry218.txt  orange38.txt      pear32.txt
# apple246.txt  banana216.txt  blackberry232.txt  orange45.txt      pear34.txt
# apple249.txt  banana21.txt   blackberry238.txt  orange51.txt      pear40.txt
# apple30.txt   banana221.txt  blackberry244.txt  orange55.txt      pear43.txt
# apple35.txt   banana225.txt  blackberry245.txt  orange75.txt      pear44.txt
# apple39.txt   banana230.txt  blackberry247.txt  orange78.txt      pear48.txt
# apple3.txt    banana231.txt  blackberry36.txt   orange79.txt      pear50.txt
# apple4.txt    banana241.txt  blackberry41.txt   orange7.txt       pear54.txt
# apple56.txt   banana243.txt  blackberry46.txt   orange92.txt      pear58.txt
# apple62.txt   banana25.txt   blackberry47.txt   orange96.txt      pear65.txt
# apple68.txt   banana26.txt   blackberry49.txt   orange97.txt      pear72.txt
# apple69.txt   banana29.txt   blackberry59.txt   orange9.txt       pear77.txt
# apple73.txt   banana2.txt    blackberry63.txt   orange.py         pear83.txt
# apple74.txt   banana31.txt   blackberry64.txt   pear0.txt         pear85.txt
# apple81.txt   banana33.txt   blackberry6.txt    pear100.txt       pear93.txt
# apple88.txt   banana37.txt   blackberry71.txt   pear101.txt
# apple91.txt   banana42.txt   blackberry86.txt   pear107.txt

In [3]: ls src/ | grep py
# apple.py
# banana.py
# orange.py

In [4]: scripts = !ls src/

In [5]: scripts.grep('py')
# Out[9]: ['apple.py', 'banana.py', 'orange.py']