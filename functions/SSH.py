import paramiko
from termcolor import colored
import time

def sshConnection(user, password):
    host = "172.16.0.10"
    port = 22
    username = "administrator"

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client = ssh.connect(host, port, user, password)
    return client



