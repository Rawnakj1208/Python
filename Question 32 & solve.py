'''
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''
def printval(n):
    if (n%2==0):
        print("It is an even number")
    elif(n%2!=0):
        print("It is a odd number")
    else:
        pass
printval(6)