'''
Question:

Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
We can define recursive function in Python.

'''
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print (f(n))