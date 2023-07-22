import sys

print('Command line arguments are: ')

for i in sys.argv:
    print(i)

print('\n\n THE PYTHON PATH IS',sys.path,'\n')


import os

print(os.getcwd())


from math import sqrt

print('Square root of 16 is ',sqrt(16))
