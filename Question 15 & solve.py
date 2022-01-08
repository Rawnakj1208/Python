'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
a=input()#for example if we take input 9
n1 = int( "%s" % a )#here we will get 9
#print(n1)
n2 = int( "%s%s" % (a,a) )#here we will get 99
#print(n2)
n3 = int( "%s%s%s" % (a,a,a) )#here we will get 999
#print(n3)
n4 = int( "%s%s%s%s" % (a,a,a,a))#here we will get 9999
#print(n4)
print(n1+n2+n3+n4)#the final out will sum of n1,n2,n3,n4 that is 11106