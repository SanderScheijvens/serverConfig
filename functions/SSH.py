import paramiko
import time

def sshConnection():
    host = "172.16.0.10"
    port = 22
    username = "administrator"
    password = "Sjiefkes120!"


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

def getStatus():
    ssh = sshConnection()
    stdin, stdout, stderr = ssh.exec_command("service jellyfin status")
    time.sleep(2)
    result = stdout.readlines()
    return result[4]

