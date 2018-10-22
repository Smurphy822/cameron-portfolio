#Cameron Murphy
#10/16/18
import math
def pythagoras_theorem(ap=1,bp=1):
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)

    print("The third side is",c)
ai=input("What is the first side?")
bi=input("What is the second side?")
pythagoras_theorem(ai,bi)




