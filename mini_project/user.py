import json
from admin import storage,orders

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add(self,flower,quantity):
        if storage[flower].stock >= quantity:
            self.flowers.append([flower,quantity])
            storage[flower].stock -=quantity
        else:
            print(f'{flower} not in stock')
    
    def remove(self,flower,quantity):
        for ele in self.flowers:
            if ele[0] == flower:
                if ele[1] == quantity:
                    self.flowers.remove(ele)
                    storage[flower].stock += quantity
                elif ele[1] >= quantity:
                    ele[1] = ele[1] - quantity
                    storage[flower].stock += quantity
                else:
                    'wrong input'

    def display(self):
        for item in self.flowers[:-1]:
            print(f'{item[0]}:{item[1]}',end =' ')
        print(f'{self.flowers[-1][0]}:{self.flowers[-1][1]}')

def place_order(username):
    state = 4
    bouquet = Bouquet()
    while state != 0:
        print('Enter option:')
        print('0:exit')
        print('1.add flower to bouquet')
        print('2.remove flower from bouquet')
        print('3.display bouquet')
        print('4.complete')
        option = int(input())
        if option == 0:
            state = 0
        elif option ==1:
            print('select flowers from below As "name quantity,":')
            i=1
            for flower in storage:
                if storage[flower].stock >0:
                    print(f'{i}:')
                    print(f'\tname:{storage[flower].name}')
                    print(f'\tprice:{storage[flower].price}')
                    print(f'\tstock:{storage[flower].stock}')
                    i+=1

            # flower_list = [(y[0],int(y[1])) for x in input().split(',') for y in x.split(' ')]
            # for flower in flower_list:
            #     bouquet.add(flower[0],flower[1])
            for x in list(input().split(',')):
                y = x.split(' ')[0]
                z = x.split(' ')[1]
                bouquet.add(y,int(z))

        elif option ==2:
            flower,quantity = input('Enter "flower,quantity" to remove: ').split(',')
            bouquet.remove(flower,int(quantity))
        
        elif option == 3:
            bouquet.display()
        
        elif option == 4:
            if username not in orders:
                orders[username] = []
            orders[username].append(bouquet)
        else:
            print('Wrong input')