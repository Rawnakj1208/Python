'''
Question:

Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].
'''
import random
print (format(random.random()*100,".02f"))
