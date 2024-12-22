# to use mathematical functions in this module first, you have to import the module
# we can import it using the following syntax
#import math
# this module includes trigonometric functions, representation functions, logarithmic functions, angle conversion, etc
#ceil(x):returns the smallest integer greater than or equal to x
#floor(x):returns the largest integer less than or equal to x
#fabs(x):returns the absolute value of x
#factorial(x):return the factorial of x
#fmod(x, y):returns the remainder when x is divided by y
#log2(x):return the base-2 logaritihm of x
#log10(x):returns the base- lagarithm of x
#pow(x,y):return x raised to the power y
#sqrt(x):returns the square root of x
#tunc(x):returns the truncated integer value of x
import math
print(math.sqrt(4))
print(math.fabs(-5))
print(math.floor(4.6))
print(math.pow(2,2))
print(math.trunc(7.999))

#random module: python has a built in random module that you can use to generate random numbers
#it defines a set of functions that are used to generate or manipulate random numnbers
#this particular type of functions is used in a lot of games, lotteries, or any application requiring 
# a random number generation
#seed(x):initialize the random number generator
#randrange(x,y,step):returns a random number betweem the given range
#randint(x,y):returns a random number between the given range
#choice(sequence):returns a random element from the given sequence
#shuffle(sequence):takes a sequence and returns the sequences in a random order
#random():returns a random float numebr between 0 and 1

#Example
import random
#generating random number between 0 and 1
print(random.random())
#generating random number between 1 and 100
print(random.randint(1,100))
#generating random number between 1 and 10
print(random.randrange(1,10))
#generating random number between 1 and 10 with step size of 2
print(random.randrange(1,10,2))

