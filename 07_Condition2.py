Devops = ["Jenkins" , "Ansible" , "Bash" , "Python" , "Pupper" , "Docker" , "Kubernetes"]
Devlopment = ("NodeJS" , "AngularJS" , "Java" , ".net" , "Python")
cntr_emp1 = {"Name" : "Santa" , "Skill" : "Blockchain" , "Code" : 1024}
cntr_emp2 = {"Name" : "Rocky" , "Skill" : "AI" , "Code" : 1218}

#Taking input from user
usr_skill = input("Enter your desired skill: ")

#Check in the database if we have the skill
if usr_skill in Devops:
    print(f"We have {usr_skill} in Devops team")
elif usr_skill in Devlopment:
    print(f"We have {usr_skill} in Devlopment team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employess with {usr_skill} skill")
else:
    print(f"{usr_skill} not found")
    print("Please check if the value enterd is correct")