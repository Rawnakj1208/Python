'''
Question:

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
Hints:
Use yield to produce the next value in generator.
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
print("Enter the Number:")
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values=[]
for i in NumGenerator(n):
    values.append(str(i))
print(",".join(values))