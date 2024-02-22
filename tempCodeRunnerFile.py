
def number_conversion_menu():
    os.system("cls || clear")
    print("\nNumber Conversion Menu")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexa to X")

def menu(): 
    os.system("cls || clear")
    print("Main Menu")
    print("\n[1] Binary Operations")
    print("[2] Number System Conversion")
    print("[3] Exit")

def is_signed():
    response = input("Is it signed? [y/n]: ")
    if response in ['y', 'Y', 'yes', 'YES', '1']:
        return True
    elif response in ['n', 'N', 'no', 'NO', '0']: