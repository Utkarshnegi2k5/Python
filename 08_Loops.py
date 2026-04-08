import time
Planet = ["Earth" , "Mercury" , "Venus"]

# For loop
for i in Planet:
    print(f"{i} is planet in solar system")

for i in Planet[0]:
    print(i)

# While loop
x = 0
while x<10:
    print(x)
    x+=1

for pal in Planet:
    print(f"The letters of Planet {pal} is:-")
    for i in pal:
        print(i)

while True:
    print("Value of x is :-")
    x+=2
    print(x)
    time.sleep(2)