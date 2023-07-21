number=23
running=True

while running:
    guess=int(input('Enter an integer: '))

    if guess==number:
        print('Congratulations! you have guessed it right!')
        running=False
    elif guess<number:
        print('No, it is little higher than that')
    else :
        print('No, it is little lower than that')
else :
    print('While loop is over')

print('Done')
