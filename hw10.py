import logging
import random
logging.basicConfig(level=logging.ERROR,filename="errorHW10.log",filemode="w",format="%(asctime)s: %(levelname)s - %(messege)s")
rangeProgres = range(0,10)
itRangeProgres = iter(rangeProgres)
progres = [(3+8*next(itRangeProgres)) for i in range(10)]
itProgres = iter(progres)
while itProgres:
    try:
        randomNum = random.randint(-5,5)
        print(next(itProgres), "/", randomNum, "=", next(itProgres) / randomNum)

    except ZeroDivisionError:
        logging.error("an error occured while dividing the progression elment by 0")
        logging.error(ZeroDivisionError)
    except StopIteration:
        logging.error("end progres")
        break