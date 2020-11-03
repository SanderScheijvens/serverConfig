import paramiko, time
from termcolor import colored

def updateUbuntu():
    host = "172.16.0.10"
    port = 22
    username = "root"
    password = ""

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command("sudo apt update && sudo apt upgrade -y")
    time.sleep(5)
    print(stdout.readlines())

def systemJellyfin():
    host = "172.16.0.10"
    port = 22
    username = "root"
    password = ""

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

    stdin, stdout, stderr = ssh.exec_command(f"sudo service jeffyfin {parameter}")
    time.sleep(5)
    print(stdout.readlines())

def systemUbuntu():
    host = "172.16.0.10"
    port = 22
    username = "root"
    password = ""

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