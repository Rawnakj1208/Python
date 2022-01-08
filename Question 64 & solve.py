'''
Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use float() to convert an integer to a float
'''
n=int(input())
sum=0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print (format(sum,'0.2f'))# we use '0.2f' for priniting 2 degit after the decimal(.)