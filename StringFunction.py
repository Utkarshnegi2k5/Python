a="Hello my name is Utkarsh"
print(a.find("Bye"))
print(len(a))
print("")
#-1 means that the string is not present
# it will give the starting index where the string is present



#Strip
a="Hello World      ,....''.........."
print(a)
print(a.rstrip(" '.,"))
print("")


# Check if the string is lower case
a="hello"
print(a.islower())
print("")


# make the string lower or upper case
a="Hello world"
print(a.lower())
print(a.upper())
print("")


#spliting
a="Hello my name is Utkarsh"
print(a.split())
print("")

a="Hello my name is Utkarsh, How are you"
print(a)
print(a.split(","))
print("")


#Find the value in string
a=input("Enter the string =")
b=input("Enter the string to find =")
if(a.find(b)==-1):
    print("Not found")
else:
    print("found at index",a.find(b))