# Flower Shop Ordering To Go - 
# Create a flower shop application which deals in flower objects 
# and use those flower objects in a bouquet object which can then be sold. 
# Keep track of the number of objects and when you may need to order more.
from utility_functions import *

def main():

    state = True

    while state:
        print('0.Exit')
        print('1.register as user')
        print('2.login as user')
        print('3.login as admin')
        option = int(input('Enter your choice: '))
        if option ==1:
            register()
        elif option ==2:
            username = input('Enter username: ')
            password = input('Enter password: ')
            while not login('user',username,password):
                username = input('Enter username: ')
                password = input('Enter password: ')
            # print('Hello user!!')
            # print('Welcome to the Flower Shop')
            user(username)
        elif option ==3:
            username = input('Enter username: ')
            password = input('Enter password: ')
            while not login('admin',username,password):
                username = input('Enter username: ')
                password = input('Enter password: ')
            admin()
        elif option ==0:
            state = False            
        else:
            print('Invalid Option')

if __name__ == '__main__':
    main()