import re
password = input('Enter your new password:\n')
mylist = []
mylist.append(re.compile('[a-z+]'))      #check for lowercase
mylist.append(re.compile('[A-Z+]'))      #check for uppercase
mylist.append(re.compile('[0-9+]'))      #check for numbers
i = 0

if len(password) >= 8:
    for items in range(len(mylist)):
        t=re.search(mylist[items], password)
        if t is not None:
            i += 1
    a= len(mylist)
    if i == a:
        print('That is a correct password')
    else:
        print('Please check that your password has all the required characters')
else:
    print('The password is too short')
