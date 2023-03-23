from models.user import User,users,orders
from models.login import Login,loggedIn

import re

def register():
    print('\n')
    fullName = input('Enter Full Name: ')
    while(not re.fullmatch('[A-Z]{1}[a-zA-Z]+ [A-Z]{1}[a-zA-Z]* [A-Z]{1}[a-zA-Z]*',fullName)):
        fullName = input('Enter Full Name: ')
    phoneNo = input('Enter Phone Number: ')
    while(not re.fullmatch('[1-9]{1}[0-9]{9}',phoneNo)):
        phoneNo = input('Enter Phone Number: ')
    email = input('Enter Email Id: ')
    while(not re.fullmatch('^[a-zA-Z0-9+_.-]+@gmail.com',email)):
        email = input('Enter Email Id: ')
    address = input('Enter Address: ')
    username = input('Enter Username: ')
    while(username in users.keys()):
        print('username already exists')
        username = input('Enter Username: ')
    while(not re.fullmatch('\w{5,}',username)):
        print('username should at least be of length 5')
        username = input('Enter Username: ')
    password = input('Enter Password: ')

    new_user = User(fullName,phoneNo,email,address,username,password)
    users[username] = new_user
    print('\nregisteration successfull\n')
    return username,password

def isValid(role,credential_obj):
    if role == 'admin':
        if credential_obj.username in loggedIn['admin'].keys():
            if loggedIn['admin'][credential_obj.username] == credential_obj.password:
                return True
            else:
                print('\nwrong password\n')
                return False
        else:
            print('\nNo admin named ',credential_obj.username)
            return False
    else:
        if credential_obj.username in loggedIn['user'].keys():
            if loggedIn['user'][credential_obj.username] == credential_obj.password:
                return True
            else:
                print('\nwrong password\n')
                return False
        else:
            print('\nNo user named ',credential_obj.username)
            return False

def login(role,username,password):
    credential =Login(username,password)

    if isValid(role,credential):
        return True
    else:
        return False
    
def checkValidity(role):
        print('\n')
        username = input('Enter username: ')
        password = input('Enter password: ')
        if login(role,username,password):
            print('\nLogin Successful !!!\n')
            return True,username
        return False,None

def checkIn(role):
    state = False
    while (role not in ['admin','user']):
        print('\n')
        print('Invalid Input !!!')
        print('Enter "user" or "admin"')
        role = input('\nEnter role(user/admin): ')
    if role == 'admin':
        state,username = checkValidity(role)
        while not state:
            print('wrong credentials\n')
            state,username = checkValidity(role)
        return role,username
    else:
        isNewUser = input('\nnew user?(y/n): ')
        while(isNewUser not in ['y','n']):
            print('Invalid Input !!!')
            print('Enter "y" or "n"\n')
            isNewUser = input('\nnew user?(y/n): \n')
        if isNewUser == 'y':
            username,password = register()
            loggedIn['user'][username] = password
            orders[username] = []
        else:
            state,username = checkValidity(role)
            while not state:
                print('wrong credentials\n')
                state,username =checkValidity(role)
        return role,username