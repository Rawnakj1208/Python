'''
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

'''
class American(object):
    @staticmethod
    def printNationality():
        print ("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
