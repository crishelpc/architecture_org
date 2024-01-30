import binary_operation
import number_conversion
import os


def binary_operations_menu(): 
    os.system("cls || clear")
    print("\nBinary Operations Menu")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")

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

menu()
option = int(input("Enter your option: "))


if option == 1: 
    binary_operations_menu()
    binary_option = int(input("Enter your option for Binary Options: "))
    if binary_option == 1: 
        binary_operation.division_binary()
    
    elif binary_option == 2: 
        binary_operation.multiply_binary()

    elif binary_option == 3: 
        binary_operation.subtract_binary()

    elif binary_option == 4: 
        binary_operation.add_binary()
    
    elif binary_option == 5: 
        binary_operation.complement()
    
    else: 
        menu()

elif option == 2: 
    number_conversion_menu()
    number_conversion_option = int(input("Enter your option for Number System Conversions:"))
    if number_conversion_option == 1: 
        number_conversion.binary_to_any()

    elif number_conversion_option == 2:
        number_conversion.decimal_to_any()

    elif number_conversion_option == 3: 
        number_conversion.octa_to_any()
    
    elif number_conversion_option == 4: 
        number_conversion.hexa_to_any()
    
    else: 
        menu()


elif option == 3: 
    exit()

else: 
    menu()