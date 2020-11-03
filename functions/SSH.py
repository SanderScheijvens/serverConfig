import paramiko
import time

def sshConnection(password):
    host = "172.16.0.10"
    port = 22
    username = "administrator"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)

def getStatus(password):
    host = "172.16.0.10"
    port = 22
    username = "administrator"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command("service jellyfin status")
    time.sleep(2)
    result = stdout.readlines()
    ssh.close()
    return result[4]

