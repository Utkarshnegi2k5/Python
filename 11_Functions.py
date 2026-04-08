def add(arg1, arg2):
    total = arg1+arg2
    return total

print(add(10,2))

def adder(a , b):
    print(a+b)

print(adder(10,2))                  # The function return None by default

def sum(arg):
    x=0
    for i in arg:
        x=x+i
    return x

l = [1,2,3,4,5]
print(sum(l))

# Default arguments
def greeting(msg="Morning"):
    print(f"Good {msg}")
    print("How are you")

greeting("Evening")


# Keyword argument
def vac(vac , efficancy):
    print(f"{vac} is having {efficancy}% efficiancy")
    if(efficancy>50) and (efficancy<75):
        print("Need more trail")
    elif(efficancy<50):
        print("Reject")
    else:
        print("Accepted")

vac("Covacine", 90)
vac(efficancy=100 , vac="unknown")                  # order dosent matter in this as we have send the data using argument keywords

