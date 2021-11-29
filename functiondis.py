#define the function ,the distance between two points
import math     #mathematical equation solve the define

def distance(x1,x2,y1,y2):
    x = x1 - x2
    x = x * x        #overwrite
    y = y1 - y2
    y = y * y        #overwrite
    x + y 

    return math.sqrt(x + y)    #fritfull function

result = distance(3,7,2,8)

print(f"the distance between two given points is {result}")