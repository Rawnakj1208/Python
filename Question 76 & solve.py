'''
Question:

Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].
'''
import random
print (random.random()*100-5)