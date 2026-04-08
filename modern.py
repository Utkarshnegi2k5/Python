def order_food(min_order , *args):
    print(f"You have order: {min_order}")
    for items in args:
        print(f"You have orderd {items}")

def vac(vac , efficancy):
    print(f"{vac} is having {efficancy}% efficiancy")
    if(efficancy>50) and (efficancy<75):
        print("Need more trail")
    elif(efficancy<50):
        print("Reject")
    else:
        print("Accepted")
