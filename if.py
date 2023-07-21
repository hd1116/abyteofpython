number=23
guess=int(input('Enter an integer: '))

if guess==number:
    # new block starts here new indent 
    print('Congratulations, you have guessed it right!')
    print('But you dont win any prizes!')
elif guess<number:
    # another block
    print('No!, its little higher than that')
else:
    print('No!, its little lower than that')

print('Done')

if True:
    print('Yes, its true checking basic if statement/control flow')