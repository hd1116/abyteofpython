def print_max(x,y):
    ''' Prints max of two numbers.
    The two values must be integers.'''
    # convert to integers if possible

    x=int(x)
    y=int(y)

    if x>y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(1,5)

print(print_max.__doc__)

