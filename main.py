import pyfiglet
from termcolor import colored
from functions import serverMenu, SSH
import getpass

user = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')

while True:
    print(75 * "-")
    ascii_banner = pyfiglet.figlet_format("MEDIA SERVER")
    print(ascii_banner)

    print(75*"-")
    print(f"{serverMenu.getStatus(user, password)}\n"
          f"{serverMenu.statusWebsite()}")
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
            serverMenu.updateUbuntu(user, password)
        elif menu_result == "2":
            serverMenu.systemJellyfin(user, password)
            print(serverMenu.getStatus(user, password))
            print()
        elif menu_result == "3":
            serverMenu.systemUbuntu(user, password)
        elif menu_result == "4":
            serverMenu.uploadMovie(user, password)
        elif menu_result == "5":
            print(colored("This option is not availible at the moment, we're working on it!\n", "red"))
        elif menu_result == "6":
            print(colored("This option is not availible at the moment, we're working on it!\n", "red"))
        elif menu_result == "exit":
            True
        else:
            print(colored("Not a valid option.\n"
                        "Please try a number out of the menu.\n", "red"))