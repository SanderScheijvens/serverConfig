import paramiko, time
from termcolor import colored
import requests
from functions import SSH
import scp

def statusWebsite():
    url = "https://media.scheijvens.com"

    status = requests.get(url)
    if status.status_code == 200:
        status_active = colored("Active", "green")
    else:
        status_active = colored("Inactive", "red")
    return f"Status Website: {status_active}"

def updateUbuntu(user, password):
    host = "172.16.0.10"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
    stdin, stdout, stderr = client.exec_command("sudo apt update && sudo apt upgrade -y")
    time.sleep(5)
    restult = stdout.readlines()
    print(restult[-1])
    client.close()

def systemJellyfin(user, password):
    host = "172.16.0.10"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
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

    stdin, stdout, stderr = client.exec_command(f"sudo service jellyfin {parameter}")
    client.close()

def systemUbuntu(user, password):
    host = "172.16.0.10"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
    parameter = ""
    option = input("reboot or shutdown?: ")
    if option.lower() == "reboot":
        parameter = "reboot"
    elif option.lower() == "shutdown":
        parameter = "shutdown now"
    else:
        print(colored("Not a valid option.\n", "red"))

    stdin, stdout, stderr = client.exec_command(f"sudo {parameter}")
    client.close()

def getStatus(user, password):
    host = "172.16.0.10"
    port = 22

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, user, password)
    stdin, stdout, stderr = ssh.exec_command("service jellyfin status")
    time.sleep(2)
    result = stdout.readlines()
    ssh.close()
    result_activity = result[4]
    result_activity = result_activity.split()
    if result_activity[1] == "failed":
        status_activity = colored(result[4].strip(), "red")
    elif result_activity[1] == "active":
        status_activity = colored(result[4].strip(), "green")
    return f"Status Server:  {status_activity}"

def uploadMovie(user, password):
    host = "172.16.0.10"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
    sftp = client.open_sftp()
    path_movies_server = "/mnt/media/movies/"

    path_movie_local = input("What is the path of the directory?: ")

    sftp.put(path_movie_local, path_movies_server)
    sftp.close()
