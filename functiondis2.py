import math
#class defination
class distance():
    #property
    #constructor
    #method
    def calculatedistance(self,x1,x2,y1,y2):
        x = x1 - x2
        x = x * x        #overwrite
        y = y1 - y2
        y = y * y        #overwrite
        x + y 

        return math.sqrt(x + y)    #fritfull function
 #lets create a class object
myobject = distance()
 #call the calculatedistance method
result = myobject.calculatedistance(4,5,7,3)
print(f"the distance between two points is {result} ")   