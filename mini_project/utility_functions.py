import json
from user import *
from admin import *

def user(username):
    state = True
    while state:
        print('Enter Option:')
        print('0.Exit')
        print('1.place order')
        print('2.view orders')
        choice = int(input())

        if choice == 0:
            state = False
        elif choice == 1:
            place_order(username)
        elif choice == 2:  
            i=1
            for order in orders[username]:
                print(i,':',end=' ')
                order.display()
                i +=1
        else:
            print('Enter valid option')

def admin():
    state = True
    while state:
        print('welcome')
        print('0.Exit')
        print('1.Add New Flower')
        print('2.Remove Flower')
        print('3.Show Inventory')
        print('4.Show orders')
        option = int(input())
        if option == 0:
            state = False
        elif option == 1:
            add_flower()
        elif option == 2:
            remove_flower()
        elif option == 3:
            show_inventory()
        elif option == 4:
            show_orders()
        else:
            print('Invalid choice')


def register():
    full_name  = input('Enter Full Name: ')
    phone_no = input('Enter Phone no.:')
    address = input('Enter Address:')
    username = input('Enter username:')
    password = input('Enter password:')

    # storing registered details

    with open('C:\\Users\\harsh\\Desktop\\Desktop\\Python Developer\\Study\\Assignments\\mini_project\\register.json','r') as file:
        registered_users = json.load(file)

    registered_users['username'] = {'full_name':full_name,'phone_no':phone_no,
                                    'address':address,'username':username,'password':password}

    with open('C:\\Users\\harsh\\Desktop\\Desktop\\Python Developer\\Study\\Assignments\\mini_project\\register.json','w') as file:
        json.dump(registered_users, file)

    print('registeration successful')

    # adding login info
    
    with open('C:\\Users\\harsh\\Desktop\\Desktop\\Python Developer\\Study\\Assignments\\mini_project\\login.json','r') as file:
        login_users = json.load(file)

    login_users['user'][username] = password

    with open('C:\\Users\\harsh\\Desktop\\Desktop\\Python Developer\\Study\\Assignments\\mini_project\\login.json','w') as file:
        json.dump(login_users,file)


def login(role,username,password):
    with open('C:\\Users\\harsh\\Desktop\\Desktop\\Python Developer\\Study\\Assignments\\mini_project\\login.json','r') as file:
        login_users = json.load(file)

    if username in login_users[role]:
        if login_users[role][username] == password:
            print('login successful')
            return True
        else:
            print('invalid password')
            return False
    print('username not found')
    return False