import random
vaccines = ["Moderna" , "Pfizer" , "Sputnik v" , "Covaxin" , "CoronaVac"]

random.shuffle(vaccines)
print(vaccines)

luck = random.choice(vaccines)
print(luck)

for vac in vaccines:
    print(f"**********Testing vaccines {vac}")
    if vac == luck:
        print(f"{luck} vaccine, Test successful")
        continue
    print("Test failed")

# Break - This will break the loop when it met the conditions.
# Continue - This will skip the further code of that iteration when it met conditions.