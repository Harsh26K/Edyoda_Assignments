from section.admin_section import admin
from section.user_section import user

from methods.accessMethods import checkIn

from models.inventory import FoodItem,foodItems
from models.user import User,users,orders
from models.login import loggedIn

def initParams():
    food1 = FoodItem('Burger(100 gm)','1pcs',60,0,10)
    food2 = FoodItem('French Fries(50 gm)','1pcs',40,0,16)
    food3 = FoodItem('Sandwich','1pcs',80,0,10)
    food4 = FoodItem('Veg Parcel','1pcs',40,0,3)
    food5 = FoodItem('Lava Cake','1pcs',40,0,2)

    foodItems['B6'] = food1
    foodItems['FF65'] = food2
    foodItems['S8'] = food3
    foodItems['VP36'] = food4
    foodItems['GB65'] = food5

    new_user = User('Test User','9577132150','test.user@gmail.com',
                    'test address','test_user','user123')
    users[new_user.username] = new_user

    loggedIn['user'][new_user.username] = new_user.password

    orders[new_user.username] = []
    order = ['Burger','French Fries','Sandwich']
    orders[new_user.username].append(order)


def app():
    initParams()
    role = input('Enter role(user/admin):')
    role,username = checkIn(role)
    print('Welcome, ',username,' to United Restaurant')
    if role == 'admin':
        option =2
        while(option !=5):
        #options
            print('\n')
            print('1. Add Food Item')
            print('2. Edit food item')
            print('3. Remove food item')
            print('4. View inventory ')
            print('5. Log out')
            print('\n')
            option = int(input('Enter your choice : '))
            print('\n')
            admin(option)
        print('Thank You, ',username)

    elif role == 'user':
        option =0
        state = False
        try:
            while(option !=5):
                print('\n')
                print('1. Place New Order' )
                print('2. Order History')
                print('3. View profile')
                print('4. Update Profile')
                print('5. Log out')
                print('\n')
                option = int(input('Enter your choice : '))
                if option == 4:
                    new_username = user(option,username)
                    print('\n')
                    print('1. Place New Order' )
                    print('2. Order History')
                    print('3. View profile')
                    print('4. Update Profile')
                    print('5. Log out')
                    print('\n')
                    option = int(input('Enter your choice : '))
                    state = True
                elif not state:
                    new_username = username
                user(option, new_username)
            print('\n Thank You, ',new_username)
        except KeyError:
            print('not found')
    else:
        print('Something went wrong')
        print('Please try again')