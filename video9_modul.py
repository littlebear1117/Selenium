
# modules and packages
# module ends in .py
# https://www.youtube.com/watch?v=aJeb1j_dlOA&t=1s

# 03/11/2017 Andrew 
# Modified on web 
# Modified on zhanga36 @ 8:18pm
# Modified on web @ 8:22pm
# Updated by pychar and checkin
# Updated by pychar and checkin again

import sys
import os
from myMudule import Person

from myPackage.Car import *

person1 = Person()
person1.name = "Brayn"
person1.sayHello()

myCar = Car()
myCar.setSpeed(100)

myTruck = Truck()
myTruck.setSpeed(90)

print (sys.version)
print (dir(os))
