name = "Utkarsh"
age = "20"

text = f"The name is {name} and the age is {age}"

print (text)

# Can print any value using index
print(text[0])

# This is slicing a string
# The string in python is indexed starting from 0
print(text[0:10:1])                         # [ start : end : jumps]
print(text[0:10:3])

# Negative indexing
print(text[-1:5:-1])                        # the indexing start from 0 to end in positive direction but can also be written from -1 at end to start in negative direction
print(text[-1:-3:-1])

########################################################################################################

# This is slicing a tuple
devops = ("Linux" , "Vagrant" , "Bash scripting" , "AWS" , "Jenkins" , "Python" , "Ansible")

# Can print a value using index
print()
print(devops[0])

print(devops[0:3:1])                        # Same as string slicing
print(devops[0:len(devops):2])              # len(devops) gives the size of tuple

# Negative indexing
print(devops[-1])

# Nested slicing
print(devops[2:5:1])                        # Devops slicing [gets tuple]
print(devops[2:5:1] [0])                    # sliced tuple get more sliced [in this case we get sting]
print(devops[2:5:1] [0] [0:7:2])            # further slice the string
print(devops[2:5:1] [0] [0:7:2] [0])        # further sliced the sliced string and we can do it more

########################################################################################################

# This is slicing a List
devops = ["Linux" , "Vagrant" , "Bash scripting" , "AWS" , "Jenkins" , "Python" , "Ansible"]

# Can print a value using index
print()
print(devops[0])

print(devops[0:3:1])                        # Same as string slicing
print(devops[0:len(devops):2])              # len(devops) gives the size of list

# Negative indexing
print(devops[-1])

# Nested slicing
print(devops[2:5:1])                        # Devops slicing [gets list]
print(devops[2:5:1] [0])                    # sliced list get more sliced [in this case we get sting]
print(devops[2:5:1] [0] [0:7:2])            # further slice the string
print(devops[2:5:1] [0] [0:7:2] [0])        # further sliced the sliced string and we can do it more

########################################################################################################

# Slicing in dictionary (not real slicing as we are using keys not index)
skills = {"devops" : ("Linux" , "Vagrant" , "Bash scripting" , "AWS") , "Devlopment":["Java" , "NodeJS" , ".net"] }
print()
print(skills)

# Printing using key 
print(skills["Devlopment"])
print(skills["Devlopment"] [-1:1:-1])
print(skills["Devlopment"] [::-1])          # This slicing can be used for reversing any list, tuple or string