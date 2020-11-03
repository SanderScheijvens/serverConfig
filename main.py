import pyfiglet, time
from termcolor import colored
from functions import serverMenu, SSH
import paramiko
import getpass


host = "172.16.0.10"
port = 22
username = "administrator"
password = getpass.getpass('Please enter your password: ')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command("service jellyfin status")
time.sleep(2)
status = stdout.readlines()

while True:
    ascii_banner = pyfiglet.figlet_format("MEDIA SERVER")
    print(ascii_banner)

    status_server = f"{status[4]}"
    status_webpage = ""

    print(75*"-")
    print(f"Status Server: {status_server}\n"
          f"Status Website: {status_webpage}")
    print(75*"-")


    print("\n1) Update Ubuntu OS\n"
          "2) Start/Stop/Restart Jellyfin Server\n"
          "3) Change IP-address server\n"
          "4) Shutdown/Reboot Ubuntu server\n"
          "5) Upload movie\n"
          "6) Upload serie\n"
          "7) Upload book\n"
    )
    print(75*"-")

    while True:
        menu_result = input("Enter an option (1-8): ")
        if menu_result == "1":
            serverMenu.updateUbuntu(password)
        elif menu_result == "2":
            serverMenu.systemJellyfin(password)
        elif menu_result == "3":
            print("This option is not availible at the moment, whe're working on it!")
        elif menu_result == "4":
            serverMenu.systemUbuntu(password)
        elif menu_result == "5":
            print("This option is not availible at the moment, whe're working on it!")
        elif menu_result == "6":
            print("This option is not availible at the moment, whe're working on it!")
        elif menu_result == "7":
            print("This option is not availible at the moment, whe're working on it!")
        else:
            print(colored("Not a valid option.\n"
                        "Please try a number out of the menu.", "red"))