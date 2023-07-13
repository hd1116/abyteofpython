age = 20
name = 'Swaroop'
# using format method
print('{0} was {1} years old when he wrote this book.'.format(name,age))
print('Why is {} playing with that Python?'.format(name))
# latest 3.6 python syntax for format method
print(f'{name} was {age} years old when he wrote the book.')
print(f'why is {name} playing with that Python?')


# decimal of (.) precision 3 (0.333)
print('{0:.3}'.format(1.0/3))
print('{0:.2}'.format(17.0/5))

# fill with underscores (_)
# text centered
print('{0:_^11}'.format('hello'))
print('{0:_^8}'.format('hd'))

# keyword based format method
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

# print always end with \n - new line character which is invisible
print('print end test')
print('a',end='')
print('b',end='')
print('c')

# escape sequence very important

print('This is first line. \nThis is second line')

# no special processing all raw

print(r'This is first line. \nThis is second line')
