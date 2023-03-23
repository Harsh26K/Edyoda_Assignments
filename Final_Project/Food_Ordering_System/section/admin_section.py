from methods.adminMethods import addFoodItem,editFoodItem
from methods.adminMethods import removeFoodItem, showFoodItems

from models.inventory import FoodItem

def admin(option):
    if option ==1:
        print('\n')
        name = input('Enter Food Name: ')
        quantity = input('Enter Quantity: ')
        price = input('Enter Price: ')
        discount = input('Enter Discount: ')
        stock = input('Enter Stock: ')
        print('\n')
        item = FoodItem(name,quantity,price,discount,stock)
        
        addFoodItem(item)

    elif option ==2:

        showFoodItems()

        foodId,prop,value = input('\nEnter foodID, name and new value:').split(',')

        editFoodItem(foodId,prop,value)

    elif option ==3:

        foodId = input('\nEnter FoodId of food to remove:')

        removeFoodItem(foodId)

    elif option ==4:

        showFoodItems()

    else:
        pass