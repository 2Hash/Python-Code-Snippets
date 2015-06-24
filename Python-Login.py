
#Author:  Eos
#Admin:   @StreamersHub.net
#Github:  https://github.com/Eos11

'''
Bugs:
Can't create more than one user or returns the user already exists.
'''

password = None
userid = None
useract = dict()
useract[userid] = password

def adduser(useract):
    user = input('Create Username: ')
    password = input('Create Password: ')
    if userid in useract:
        print ("That user already exsist")
        return False
    else:
        print("Successfully Created Account")
        useract[userid] = password
        return True

usercreation = dict()
for i in range(15):
    adduser(usercreation)

     
