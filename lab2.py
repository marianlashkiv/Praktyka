from math import *
a=0.1
while True:
    if a <= 0.9:
        x=a
        y=acos(x)/(2*x+1)
        print (y)
    else:
        break
    a=a+0.1
