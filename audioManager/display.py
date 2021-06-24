import os

def print_menu():
    print("-"*30)
    print("** Audio Manager **")
    print("-"*30)

    print("[1] Register Album")
    print("[2] Register Song")
    print("[3] Print Catalog")
    print("[4] Count all the song in the system")
    print("[5] Total $ in the Catalog")

    print("[q] Quit")


def clear():
    if(os.name=="nt"):
        os.system("cls")
    else:
        os.system("clear")

    #os.system("cls" if os.name == "nt" else "clear")

def print_header(text):
    clear()
    print("-"*30)
    print(text)
    print("-"*30)


    """
    Song
    id
    title
    lentght secs
    author
    """