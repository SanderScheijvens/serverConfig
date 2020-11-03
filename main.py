import pyfiglet
import time
from termcolor import colored
from functions import serverMenu, SSH
import paramiko
import getpass

password = getpass.getpass('Please enter your password: ')

status_server = SSH.getStatus(password)
status_website = serverMenu.statusWebsite()

while True:
    print(75 * "-")
    ascii_banner = pyfiglet.figlet_format("MEDIA SERVER")
    print(ascii_banner)

    status_server = f"{status_server.strip()}"
    status_webpage = f"{status_website}"

    print(75*"-")
    print(f"Status Server:    {status_server}\n"
          f"Status Website:   {status_webpage}")
    print(75*"-")


    print("\n1) Update Ubuntu OS\n"
          "2) Start/Stop/Restart Jellyfin Server\n"
          "3) Shutdown/Reboot Ubuntu server\n"
          "4) Upload movie\n"
          "5) Upload serie\n"
          "6) Upload book\n"
          "exit) Exit program"
    )
    print(75*"-")

    while True:
        menu_result = input("Enter an option (1-8): ")
        if menu_result == "1":
            serverMenu.updateUbuntu(password)
        elif menu_result == "2":
            serverMenu.systemJellyfin(password)
            print(colored(SSH.getStatus(password).strip(), ['green']))
            print()
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
        elif menu_result == "exit":
            True
        else:
            print(colored("Not a valid option.\n"
                        "Please try a number out of the menu.", "red"))