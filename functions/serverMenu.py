import paramiko, time
from termcolor import colored
import urllib.request

def statusWebsite():
    url = "https://media.scheijvens.com"

    code = urllib.request.urlopen(url).getcode()

    if code == 200:
        return colored("Active", "green")
    else:
        return colored("Inactive", "red")



def updateUbuntu(password):
    host = "172.16.0.10"
    port = 22
    username = "root"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command("sudo apt update && sudo apt upgrade -y")
    time.sleep(5)
    restult = stdout.readlines()
    print(restult[-1])
    ssh.close()

def systemJellyfin(password):
    host = "172.16.0.10"
    port = 22
    username = "root"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

    parameter = ""
    option = input("Start, stop or restart?: ")
    if option.lower() == "start":
        parameter = "start"
    elif option.lower() == "stop":
        parameter = "stop"
    elif option.lower() == "restart":
        parameter = "restart"
    else:
        print(colored("Not a valid option.\n", "red"))

    stdin, stdout, stderr = ssh.exec_command(f"sudo service jellyfin {parameter}")
    ssh.close()

def systemUbuntu(password):
    host = "172.16.0.10"
    port = 22
    username = "root"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

    parameter = ""
    option = input("reboot or shutdown?: ")
    if option.lower() == "reboot":
        parameter = "reboot"
    elif option.lower() == "shutdown":
        parameter = "shutdown now"
    else:
        print(colored("Not a valid option.\n", "red"))

    stdin, stdout, stderr = ssh.exec_command(f"sudo {parameter}")
    ssh.close()