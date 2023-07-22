# ab is shortcut for addressbook

ab={ 'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'}

print('Swaroops email address is',ab['Swaroop'])

print('Removing Spammer contact')

del ab['Spammer']

print('Now there are {} contacts in the addressbook'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

print("Added Guido's contact")

if 'Guido' in ab:
    print("Guido's address is",ab['Guido'])

