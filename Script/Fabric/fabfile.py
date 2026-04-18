from fabric.api import *
def greetings(msg):
    print(f"Hello {msg}")

def system_info():
    print("Disk space")
    local("df -h")                  # "local" is the function in fabric module use to run command on local machine
    print("Memory -m")
    local("free -m")
    print("System uptime")
    local("uptime")

def remote_exec():
    run("hostname")
    run("uptime")