import paramiko
from termcolor import colored
import time

def sshConnection(user, password):
    host = "172.16.0.10"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)




