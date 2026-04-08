# Variable Length Argument *args (Non keyword argument)
def order_food(min_order , *args):
    print(f"You have order: {min_order}")
    for items in args:
        print(f"You have orderd {items}")

order_food("Salad" , "Pizza" , "Coke")

# Variable Length Argument **kwargs (Keyword argument)
def dic(**kwargs):
    print (kwargs.keys())
dic(Name = "Utkarsh" ,Age = 20)