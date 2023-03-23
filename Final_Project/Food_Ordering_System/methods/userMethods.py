from models.user import users,orders
from models.inventory import foodItems

import pandas as pd

def dataFrame():
    foodId = [key for key in list(foodItems.keys())]
    Name = [foodItems[key].name for key in list(foodItems.keys())]
    Quantity = [foodItems[key].quantity for key in list(foodItems.keys())]
    Price = [foodItems[key].price for key in list(foodItems.keys())]
    Discount = [foodItems[key].discount for key in list(foodItems.keys())]
    Stock = [foodItems[key].stock for key in list(foodItems.keys())]
    d = {'foodId':foodId,'Name':Name,'Quantity(pcs)':Quantity,'Price(Rs.)':Price,
        'Discount(%)':Discount,'Stock':Stock}
    df = pd.DataFrame(data=d)
    return df

def placeOrder(username):
    lst = [x for x in input('\nEnter the dishes: ').split(',')]
    order = []
    for i in lst:
        food = foodItems[list(foodItems.keys())[int(i)-1]].name
        order.append(food)
        foodItems[list(foodItems.keys())[int(i)-1]].stock -= 1
    orders[username].append(order)
    print('Order placed successfully')
    for i in range(len(order)-1):
        print(order[i],end=',')
    print(f'{order[-1]} added to your order' )

def orderHistory(username):
    lst = orders[username]
    for i in range(len(lst)):
        print('\norder ',i+1,' :')
        for j in range(len(lst[i])):
            print(j+1,' : ',lst[i][j])

def profile(user_obj):
    print('\n')
    print(f'1. Full Name : {user_obj.name}')
    print(f'2. Phone No.: {user_obj.phoneNo}')
    print(f'3. email:{user_obj.email}')
    print(f'4. Address: {user_obj.address}')
    print(f'5. Username:{user_obj.username}')
    print(f'6. Password: {user_obj.password}')
    print('\n')

def updateProfile(user_obj,num,value):
    if int(num) ==1:
        users[user_obj.username].name = value
    elif int(num) ==2:
        users[user_obj.username].phoneNo = value
    elif int(num) ==3:
        users[user_obj.username].email = value
    elif int(num) ==4:
        users[user_obj.username].address = value
    elif int(num) ==5:
        prev = user_obj.username
        if value in users.keys():
            return False
        users[value] = users[user_obj.username]
        users[value].username = value
        orders[value] = orders[prev]
        del users[prev]
        del orders[prev]
        return user_obj,value
    elif int(num) ==6:
        users[user_obj.username].password = value
    else:
        print('wrong input')
    print('\n')
    print('Profile:')
    return user_obj

def showFoodItems():
    # print('| Id | Name | Quantity | Price(Rs.) | Discount(%) | Stock |')
    # for key in foodItems.keys():
    #     print(f'| {key} | {foodItems[key].name} | {foodItems[key].quantity} | {foodItems[key].price} | {foodItems[key].discount} | {foodItems[key].stock} |')

    df = dataFrame()
    df = df[['Name','Quantity(pcs)','Price(Rs.)','Discount(%)']][df['Stock'] >0]

    for i in range(df.shape[0]):
        print(f'{i+1}. {df["Name"][i]} ( {df["Quantity(pcs)"][i]} ) [{df["Price(Rs.)"][i]*(1-(df["Discount(%)"][i]/100))}]')

