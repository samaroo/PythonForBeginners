# Notes
# Functions in "Math" Library
# use "import math" to import math library
# abs(x) will return the absolutw calue of x
# "math.ceil(x)" will round x up to the nearest integer greater than it
# "math.floor(x)" will round x down to the nearest integer less than it
# "pow(x, y)" will return x^y
# 
# Functions in "Random" Library
# "random.choice(x)" where x is a list or tuple will return a random element of x 
# "random.randrange(x, y)" will return a random elements between x and y
# "random.shuffle(x)" where x is a list or tuple, will shuffle x

import math
import random

# Find the hypotnuse of a triangle with sides 15 and 17

print(math.hypot(15, 17))

# convert degrees to radians and radians to degrees

print(math.radians(180))
print(math.degrees(2))
print(math.radians(270))
print(math.degrees(5))

# generate 100 random numbers between 1 and 10

sum = 0;
x = 100
for i in range(x):
    num = random.randrange(1,10)
    sum += num
    print(num)

print("The sum is: ", sum)
print("The average is: ", sum / x)