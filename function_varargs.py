def total(a=5,*numbers,**phonebook):
    print('a',a)

    # iterate through all the items in the tuple

    for single_item in numbers:
        print('single item',single_item)
    
    # iterate through all the items in the dictionary

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)
    

total(10,1,2,3,Jack=1111,John=2231,Inge=1560)
