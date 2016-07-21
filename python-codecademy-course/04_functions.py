### Unit 4 - Functions
### https://www.codecademy.com/courses/python-beginner-c7VZg/2/1?curriculum_id=4f89dab3d788890003000096

import math

## 1. I Know Kung Fu
print(math.sqrt(25))


## 2. Generic Imports
## Previous example doesn't work without importing 'math" module
import math
print(math.sqrt(25))


## 3. Function Imports
## It's even better to just import function that we need
from math import sqrt
print(sqrt(25))


## 4. Universal imports
## Handy if we need all functions and variables from module
## However, they are usually not a good idea
from math import *


## 5. Here be dragons
import math
everything = dir(math)
print everything


## 6. On Beyond Strings
def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


## 6. max()
maximum = max(-10, 101.4, 100)
print(maximum)


## 7. min()
minimum = min(-101.4, 101, 200)
print(minimum)


## 8. abs()
absolute = abs(-42)
print(absolute)


## 9. type()
print(type(42))
print(type(4.2))
print(type('spam'))


## 10. Review: functions
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("i don't know"))


## 11. Review: modules
import math
print(math.sqrt(13689))


## 12. Review: Built-in functions
def distance_from_zero(num):
    if type(num) == float or type(num) == int:
        return abs(num)
    else:
        return "Nope"

print(distance_from_zero(1001))
