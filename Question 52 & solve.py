'''
Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
'''
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print (aCircle.area())
#print (round(aCircle.area()))#if we want to get a round value instate of flot value we can use round