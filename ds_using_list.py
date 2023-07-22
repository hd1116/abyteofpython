# this is my shopping list

shoplist=['mango','banana','apple','carrot']

print('I have',len(shoplist),'items to purchase')

print('These items are:')

for i in shoplist:
    print(i)

print('I also have to buy Rice')

shoplist.append('rice')

print('My shopping list is now ',shoplist)

print('I will sort my list now')

shoplist.sort()

print('My sorted shopping list is now',shoplist)

print('The first item in my shoplist is ',shoplist[0])

olditem=shoplist[0]

del shoplist[0]

print('I bought ',olditem)

print('Now my shopping list is ',shoplist)

