from fabric.api import *
import os
def web(WebUrl , DirName):
    sudo("yum install httpd wget unzip zip -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    
    local("apt install zip unzip")
    local(f"wget -o website.zip {WebUrl}")
    local("unzip website.zip")

    with lcd(DirName):
        local("zip -r toplate.zip *")
        put("toplate.zip" , "/var/www/html/" , use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip -o toplate.zip")
    
    sudo("systemctl restart httpd")
    print("Website is done")