import random
from datetime import datetime

def create(_start,end):
    irancell = ("938" , "936" , "935" , "939" , "939")
    hamrahaval = ("911" , "912" , "919" , "915")
    _QW = "+98"
    _next = "\n"
    while _start < end:
        taknum = random.choice(range(0,9+1))
        taknum2 = random.choice(range(0,9+1))
        numbers = list(range(1000000,9999999))
        number = str(random.choice(numbers))
        incl = _QW + random.choice(irancell) + number
        hamrah = _QW + random.choice(hamrahaval) + number
        if len(incl) == 12:
            incl = incl + str(taknum)
        if len(hamrah) == 12:
            hamrah = hamrah + str(taknum)
        if len(incl) == 11:
            incl = incl + str(taknum)  + str(taknum2)
        if len(hamrah) == 11:
            hamrah = hamrah + str(taknum) + str(taknum2)
        with open("irancell.txt","a") as wr:
            wr.write(incl+_next)
        with open("hamrahaval.txt","a") as wrh:
            wrh.write(hamrah+_next)
            _start = _start + 1
            
n = datetime.now()
create(0,10)
print('Done:',datetime.now()-n)
