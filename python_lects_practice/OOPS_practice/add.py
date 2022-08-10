import logging as lg
import os


def addition(*args):
    lg.basicConfig(filename="test.log", level=lg.DEBUG)
    try:
        sum = 0
        lg.info("\n\n------------------<<<   new instance    >>>----------------")
        for i in args:
            lg.info("starting to add number " + str(i))
            sum += i
            lg.info("cumulative sum : " + str(sum))
        lg.info("\t\t\tsum done... ans = " + str(sum))
        return sum
    
    except Exception as e:
        lg.debug("bhai string ka int ke sath addition nahi karte")
        lg.error(str(e))

print(addition(1,4,6,8,9,900,2,34,5))
print(addition('fsa',1243))