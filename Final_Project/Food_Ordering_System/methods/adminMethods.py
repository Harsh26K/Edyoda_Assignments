from models.inventory import foodItems
import pandas as pd

def generateFoodID(name):
    foodID = ''
    count = []
    c=0
    for i in name:
        if i.isupper():
            foodID+=i
            c+=1
        elif i ==' ':
            count.append(str(c))
            c=0
        else:
            c+=1
    count.append(str(c))
    return foodID+''.join(count)

def addFoodItem(item):
    foodID = generateFoodID(item.name)
    foodItems[foodID] = item
    print(f'\nsuccessfully added {foodItems[foodID].name}')

def editFoodItem(id,param,value):
    if param == 'Name':
        foodItems[id].name = value
        print(f'\nName for {id} changed to {value}')
    elif param == 'Quantity':
        foodItems[id].quantity = value
        print(f'\nQuantity for {id} changed to {value}')
    elif param == 'Price(Rs.)':
        foodItems[id].price = value
        print(f'\nPrice for {id} changed to {value}')
    elif param == 'Discount(%)':
        foodItems[id].discount = value
        print(f'\nDiscount for {id} changed to {value}')
    elif param == 'Stock(pcs)':
        foodItems[id].stock = value
        print(f'\nStock for {id} changed to {value}')
    else:
        print('No column named ',param)

def removeFoodItem(id):
    if id in foodItems.keys():
        print(id,' removed successfully')
        del foodItems[id]
    else:
        print(id,'not found')


def showFoodItems():
    # print('| Id | Name | Quantity | Price(Rs.) | Discount(%) | Stock |')
    # for key in foodItems.keys():
    #     print(f'| {key} | {foodItems[key].name} | {foodItems[key].quantity} | {foodItems[key].price} | {foodItems[key].discount} | {foodItems[key].stock} |')
    foodId = [key for key in list(foodItems.keys())]
    Name = [foodItems[key].name for key in list(foodItems.keys())]
    Quantity = [foodItems[key].quantity for key in list(foodItems.keys())]
    Price = [foodItems[key].price for key in list(foodItems.keys())]
    Discount = [foodItems[key].discount for key in list(foodItems.keys())]
    Stock = [foodItems[key].stock for key in list(foodItems.keys())]
    d = {'foodId':foodId,'Name':Name,'Quantity':Quantity,'Price(Rs.)':Price,
        'Discount(%)':Discount,'Stock(pcs)':Stock}
    df = pd.DataFrame(data=d)
    print(df)