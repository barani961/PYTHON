
menu= {
    "coffee":{
            "ingridients":{
                'water':50,
                'milk':100,
                 'coffee':40
                            },
        "cost":200,
             },
    "tea":{
        "ingridients":{
            'water':150,
            'milk':200,
            'coffee':50
            
                        },
        "cost":150,
            },
    
    "cappacino":{
        "ingridients":{
            'water':50,
            'milk':300,
            'coffee':140
                        },
        'cost':300,
                    }
    }
            
profit=0
resource={
    'water':500,
    'milk':200,
    'coffee':100
    }

def check_resources(order_ingridients):
    for item in order_ingridients:
        pass

is_on =True
while is_on==True:
    choice=input("what do you like to have?(coffee/tea/cappacino):")
    if choice =='off':
        is_on=False
    elif choice=='report':
        print(" water: ",resource['water'],"ml"," \n milk:", resource['milk'] ,"ml","\n coffee:",resource['coffee'],"g","\n profit:Rs.",profit)
    else:
        typ=menu[choice]
        print(typ)
        check_resources(typ['ingridients'])
        
