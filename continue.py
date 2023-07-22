while True:
    s=input('Please enter something: ')
    if s=='quit':
        break
    if len(s)<3:
        print('Too Small')
        continue
    print('Input is of sufficient length')

print('Done')
