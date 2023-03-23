from methods.userMethods import placeOrder,orderHistory,showFoodItems
from methods.userMethods import profile,updateProfile

from models.user import users

def user(option,username):
    if option ==1:

        showFoodItems()
        placeOrder(username)

    elif option ==2:

        orderHistory(username)

    elif option ==3:

        user_obj = users[username]
        profile(user_obj)

    elif option ==4:

        user_obj = users[username]
        profile(user_obj)
        num,value = input('\nEnter number and updated value:').split(',')
        if int(num) in [1,2,3,4,6]:
            user_obj = updateProfile(user_obj,num,value)
        elif int(num) ==5:
            user_obj,new_username = updateProfile(user_obj,num,value)
            return new_username
        else:
            print('\nwrong number')
        while(user_obj == False):
            print('Username already taken')
            user_obj = updateProfile(user_obj,num,value)
        profile(user_obj)
        return user_obj.username
    
    elif option==5:
        return
    else:
        print('\nwrong input!!!!')