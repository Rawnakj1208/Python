'''
Question:

    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

Hints:
    The built-in document method is __doc__

'''
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)


def square(num):
    '''Return the square value of the input number.

    The input number must be integer.
    '''
    return num ** 2


print (square(2))
print(square.__doc__)