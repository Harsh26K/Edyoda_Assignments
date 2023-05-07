import json
# flower inventory
storage = {}
orders = {}
class Flower:
    def __init__(self,name,stock,price):
        self.name = name
        self.stock = stock
        self.price = price

def add_flower():
    name = input('Enter Flower Name:')
    price = int(input('Enter Price:'))
    stock = int(input('Enter Stock:'))
    flower = Flower(name,stock,price)
    # if flower is already in storage update only stock value
    # else add the new flower object
    if name in storage:
        storage[flower.name].stock += flower.stock 
    else:
        storage[flower.name] = flower

def remove_flower():
    name = input('Enter flower name to remove:')
    try:
        del storage[name]
    except KeyError:
        print('no flower named',name)

def show_inventory():
    print('Inventory:')
    i=1
    for flower in storage:
        print(f'{i}:')
        print(f'\tname:{storage[flower].name}',end = ' ')
        print(f'\tprice:{storage[flower].price}',end=' ')
        print(f'\tstock:{storage[flower].stock}')
        i+=1

def show_orders():
    if len(orders):
        i=1
        for user in orders:
            print(f'{i}:',end =' ')
            for order in orders[user]:
                print(f'\tname:{user}',end =' ')
                print(f'\tBouquet:',end=' ')
                order.display()
    else:
        print('No orders yet')