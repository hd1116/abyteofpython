import re 

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text==reverse(text)

something=input('Please enter something ')
something1=re.sub(r'\W+\s*', ' ', something)
something2=something1.replace(' ','')
something3=something2.lower()


if is_palindrome(something3):
    print('Yes its a palindrome')
else:
    print('No, its not a palindrome')




