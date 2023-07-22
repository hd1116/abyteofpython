poem='''\
Programming is fun
when work is done
If you wanna make your work also fun:
Use Python!
    '''

# open for writing

f=open('poem.txt','w')

# write text to file

f.write(poem)

# close the file

f.close()

# if no mode is specified default read mode

f=open('poem.txt')

while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
# close the file

f.close()
