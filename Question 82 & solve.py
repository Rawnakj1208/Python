'''
Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''

import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))