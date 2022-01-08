'''
Question:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

'''
from appdirs import unicode

s = input()
u = unicode(s)#, "utf-8")
print(u)
