import string
text = "utkarsh is hero"

print(text.capitalize())
print(text.upper())
print(text.islower())

print(text.find("utkarsh"))

seq = ("Utkarsh" , "is" , "my" , "name")
print(" ".join(seq))

seq = ("192" , "168" , "32" , "5")
print(".".join(seq))

ls = ["Utkarsh" , "Ayush" , "Tripti"]
ls2 = ["Kartik" , "Yuvraj"]

print(ls)
ls.append("Pranjal")
print(ls)

ls.extend(ls2)
print(ls)

ls.insert(3 , "Parm")
print(ls)

ls.pop()
print(ls)

ls.pop(3)
print(ls)

cntr_emp = {"Name" : "Utkarsh" , "Skill" : "Devops"}
print(cntr_emp.keys())
print(cntr_emp.values())
print(cntr_emp.items())
cntr_emp["Id_no"] = 45
print(cntr_emp)