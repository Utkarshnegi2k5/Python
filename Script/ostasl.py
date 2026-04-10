#! /usr/bin/python3
import os

#To check and add user
UserList = ["Utkarsh" , "Vivek"]

print("Adding user to system")
print("#############################################")

for user in UserList:
    Exitcode = os.system(f"id {user}")
    if Exitcode != 0:
        print(f"User {user} does not exist. Adding it :-")
        os.system(f"useradd {user}")
        print("#####################################3")
    else:
        print(f"User {user} already exist.")
        print("#####################################3")

#To check and add user to group

Exitcode = os.system("grep Student /etc/group")
if Exitcode != 0:
    print("Group Student does not exist. Adding it:-")
    os.system("groupadd Student")
    print("#####################################3")

else:
    print("Group already exist")
    print("#####################################3")

for user in UserList:
    print(f"Adding user {user} in Student group")
    os.system(f"usermod -G Student {user}")
    print("#####################################3")


# Making directory and giveing permission and ownership to it
if os.path.isdir("/opt/Student_dir"):
    print("Directory already exist")
else:
    os.mkdir("/opt/Student_dir")

print("Assigning permission and ownership to the directory")
os.system("chown :Student /opt/Student_dir")
os.system("chmod 770 /opt/Student_dir")